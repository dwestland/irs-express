# -*- coding: utf-8 -*-

"""
    This file contains code of Celery's tasks for importing fresh data for "IRS Local and National Standards Tables".

    Disclaimer: This file has some 'dirty' solutions for parsing data from PDF files or web pages.
    Data parsing is always tricky and I am sorry if it remains unclear despite of comments.
"""

import os
import re
import datetime
import requests
from celery import shared_task
import logging
import lxml.html

from django.utils import timezone
from django.db import transaction

from .models import (County,
                     HousingUtilitiesStandard, FoodClothingStandard, OutOfPocketHealthCare, TransportationStandard,
                     DocumentStatus)
from .exceptions import DocParseError
from .utils import parse_pdf, get_num_from_elem
from .const import TRANSPORTATION_TAX_TYPE, STATE_CODE2NAME

logger = logging.getLogger(__name__)

digfree_re = re.compile(r'([^\s\t,\d]+)([\d]+(?:,\d+)?)', re.I)
fcs_updated_re = re.compile(r'updated: (\d+-\w+-\d+)', re.I)
ophc_updated_re = re.compile(r'updated: (\d+-\w+-\d+)', re.I)
transp_updated_re = re.compile(r'updated: (\d+-\w+-\d+)', re.I)
t_region_re = re.compile(r'^(\w+?) Census Region:\s+(.+)$', re.I)

# Housing and Utilities Standards - using PDF file parsing. Do web page(s) parsing if PDF produces issues
ashs_file_url = 'http://www.irs.gov/pub/irs-utl/all_states_housing_standards.pdf'
ashs_page_url = \
    'https://www.irs.gov/Businesses/Small-Businesses-&-Self-Employed/Local-Standards-Housing-and-Utilities'

# FoodClothingStandard - using web page parsing
fcs_file_url = 'https://www.irs.gov/pub/irs-utl/national_standards.pdf'
fcs_page_url = \
    'https://www.irs.gov/Businesses/Small-Businesses-&-Self-Employed/National-Standards-Food-Clothing-and-Other-Items'

# Out-of-Pocket Health Care - using web page parsing
ophc_file_url = 'https://www.irs.gov/pub/irs-utl/out-of-pocket_health_care.pdf'
ophc_page_url = \
    'https://www.irs.gov/Businesses/Small-Businesses-&-Self-Employed/National-Standards-Out-of-Pocket-Health-Care'

# Transportation Standards - using web page parsing, PDF file is incomplete
transp_file_url = 'https://www.irs.gov/pub/irs-utl/transportation_standards.pdf'
transp_page_url = 'https://www.irs.gov/Businesses/Small-Businesses-&-Self-Employed/Local-Standards-Transportation'


def report_error(source):
    # TODO
    pass


@transaction.atomic
def proceed_ashs_file(force=False):
    logger.info("get_ashs_file: Start task get_ashs_file")
    # check for updates
    resp = requests.get(ashs_page_url)
    if not resp.ok:
        raise DocParseError("get_ashs_file: Cannot retrieve the file: HTTP Code %s: %s"
                            % (resp.status_code, resp.content))
    doc = lxml.html.fromstring(resp.content)
    if not force:
        # check when the page was modified
        ashs_docstatus = DocumentStatus.objects.filter(document_name=HousingUtilitiesStandard.__name__)
        if len(ashs_docstatus) > 0:
            ashs_docstatus = ashs_docstatus[0]
            page_mdf_elem = doc.xpath('//div[@class="modified"]')[0]
            updated_on = ashs_updated_re.findall(page_mdf_elem.text)[0]
            updated_on = datetime.datetime.strptime(updated_on, '%d-%b-%Y')
            if ashs_docstatus.success_time > updated_on:
                logger.info("get_ashs_file: Page was modified on %s but already scanned on %s. Skip processing" %
                            (updated_on.strftime('%d-%m-%Y'), ashs_docstatus.success_time.strftime('%d-%m-%Y')))
                return False
    # get the data
    resp = requests.get(ashs_file_url)
    if not resp.ok:
        raise DocParseError("get_ashs_file: Cannot retrieve the file: HTTP Code %s: %s"
                            % (resp.status_code, resp.content))
    # convert to tsv
    tsvdata = parse_pdf(resp.content.decode('latin-1'))
    logger.info("get_ashs_file: PDF parsing completed")
    # cleanup received data
    tsvdata = tsvdata.split('\n')
    newdata = []
    # list of substrings to ignore in parsing
    known_garbage_st = ["Housing and", "Please note that", "latest version",
                        "Utilities for a", "Family of", "State Name"]
    # Below is a bit dirty, but working (at the current time) solution. All claims - to PDF format, please

    counties_cache = {}
    for county in County.objects.all().values_list('id', 'state_name', 'name'):
        counties_cache["{1}_{2}".format(*county)] = county[0]
    new_counties, items_processed = 0, 0

    for rawline in tsvdata:
        if not rawline:
            continue
        line = rawline
        # The line with 'ColumbiaDistrict' is too long and words get glued. We're breaking them
        if "ColumbiaDistrict" in line:
            line = line.replace("ColumbiaDistrict", "Columbia\tDistrict")
        # split joined cells (with words and numbers next) if any
        line = digfree_re.sub('\g<1>\t\g<2>', line)
        columns = line.replace(',', '').split("\t")
        if len(columns) < 7:
            for grb in known_garbage_st:
                if grb in line:
                    break
            else:
                # look after the logs for these strings from time to time to be sure no new not processed items
                logger.debug("get_ashs_file: Skip SHORT line: '%s'" % line)
            continue
        if not all(c.isdigit() for c in columns[-5:]):
            # Look after this too
            logger.debug("get_ashs_file: Skip line: '%s'" % line)
            continue
        # It seems we are ready to extract the data!
        state_name = columns[0]
        county_name = " ".join(columns[1:len(columns) - 5])
        county_name = county_name.replace(" County", '')
        family_prices = columns[-5:]

        # Filling up database
        county_cache_key = "%s_%s" % (state_name, county_name)
        county_id = counties_cache.get(county_cache_key)
        if not county_id:
            new_county = County.objects.create(state_name=state_name, name=county_name)
            new_counties += 1
            county_id = new_county.id
            counties_cache[county_cache_key] = county_id
        hus, created = HousingUtilitiesStandard.objects.update_or_create(county_id=county_id, defaults={
            'family1': family_prices[0],
            'family2': family_prices[1],
            'family3': family_prices[2],
            'family4': family_prices[3],
            'family_more': family_prices[4],
        })
        items_processed += 1
    DocumentStatus.objects.update_or_create(
        document_name=HousingUtilitiesStandard.__name__,
        defaults={'success_time': timezone.now(), 'scheduled': False}
    )
    logger.info("get_ashs_file: Done. Created %s new counties, processed %s items" % (new_counties, items_processed))
    return True


@transaction.atomic
def proceed_fcs_file(force=False):
    logger.info("get_fcs_file: Start task get_fcs_file")
    # get the data
    resp = requests.get(fcs_page_url)
    if not resp.ok:
        raise DocParseError("get_fcs_file: Cannot retrieve the file: HTTP Code %s: %s"
                            % (resp.status_code, resp.content))
    doc = lxml.html.fromstring(resp.content)
    if not force:
        # check when the page was modified
        fcs_docstatus = DocumentStatus.objects.filter(document_name=FoodClothingStandard.__name__)
        if len(fcs_docstatus) > 0:
            fcs_docstatus = fcs_docstatus[0]
            page_mdf_elem = doc.xpath('//div[@class="modified"]')[0]
            updated_on = fcs_updated_re.findall(page_mdf_elem.text)[0]
            updated_on = datetime.datetime.strptime(updated_on, '%d-%b-%Y')
            if fcs_docstatus.success_time > updated_on:
                logger.info("get_fcs_file: Page was modified on %s but already scanned on %s. Skip processing" %
                            (updated_on.strftime('%d-%m-%Y'), fcs_docstatus.success_time.strftime('%d-%m-%Y')))
                return False
    # remember existing IDs to delete those not updated
    all_ids = set(FoodClothingStandard.objects.all().values_list('id', flat=True))
    used_ids = []

    # There were only two tables on the page, but we're trying to find by first column's text
    # Find a table on the page
    trs1 = doc.xpath('//table//th[text()="Expense"]/../../tr')
    trs2 = doc.xpath('//table//th[text()="More than four persons"]/../../tr')
    total_additional = get_num_from_elem(trs2[1][1])
    for row in trs1:
        th, p1, p2, p3, p4 = row
        if th.tag != 'th':
            raise DocParseError("get_fcs_file: Unexpected table structure on the page")
        if p1.tag != 'td':
            continue
        additional_person = 0
        if th.text == 'Total':
            additional_person = total_additional
            # continue
        obj, created = FoodClothingStandard.objects.update_or_create(expense=th.text, defaults={
            'family1': get_num_from_elem(p1),
            'family2': get_num_from_elem(p2),
            'family3': get_num_from_elem(p3),
            'family4': get_num_from_elem(p4),
            'additional_person': additional_person,
        })
        used_ids.append(obj.pk)
    old_ids = all_ids - set(used_ids)
    if old_ids:
        logger.debug("get_fcs_file: Delete %s old ids" % (len(old_ids)))
        FoodClothingStandard.objects.filter(id__in=old_ids).delete()
    # update success
    DocumentStatus.objects.update_or_create(
        document_name=FoodClothingStandard.__name__,
        defaults={'success_time': timezone.now(), 'scheduled': False}
    )
    logger.info("get_fcs_file: Done. Processed %s items" % (len(used_ids)))
    return True


@transaction.atomic
def proceed_ophc_file(force=False):
    logger.info("get_ophc_file: Start task get_ophc_file")
    # get the data
    resp = requests.get(ophc_page_url)
    if not resp.ok:
        raise DocParseError("get_ophc_file: Cannot retrieve the file: HTTP Code %s: %s"
                            % (resp.status_code, resp.content))
    doc = lxml.html.fromstring(resp.content)
    if not force:
        # check when the page was modified
        ophc_docstatus = DocumentStatus.objects.filter(document_name=OutOfPocketHealthCare.__name__)
        if len(ophc_docstatus) > 0:
            ophc_docstatus = ophc_docstatus[0]
            page_mdf_elem = doc.xpath('//div[@class="modified"]')[0]
            updated_on = ophc_updated_re.findall(page_mdf_elem.text)[0]
            updated_on = datetime.datetime.strptime(updated_on, '%d-%b-%Y')
            if ophc_docstatus.success_time > updated_on:
                logger.info("get_ophc_file: Page was modified on %s but already scanned on %s. Skip processing" %
                            (updated_on.strftime('%d-%m-%Y'), ophc_docstatus.success_time.strftime('%d-%m-%Y')))
                return False
    # remember existing IDs to delete those not updated
    all_ids = set(OutOfPocketHealthCare.objects.all().values_list('id', flat=True))
    used_ids = []

    # Find a table on the page
    trs = doc.xpath('//table//th[text()="Out-of-Pocket Costs"]/../../../tbody/tr')
    if not trs:
        raise DocParseError("get_ophc_file: Unexpected table structure on the page: no rows")
    for row in trs:
        th, p = row
        if th.tag != 'th':
            raise DocParseError("get_ophc_file: Unexpected table structure on the page")
        if p.tag != 'td':
            continue
        if th.text == 'Under 65':
            obj, created = OutOfPocketHealthCare.objects.update_or_create(
                max_age=64, defaults={'cost': get_num_from_elem(p)})
        elif th.text == '65 and Older':
            obj, created = OutOfPocketHealthCare.objects.update_or_create(
                max_age=1000, defaults={'cost': get_num_from_elem(p)})
        else:
            logger.warn("get_ophc_file: Unknown row: '%s | %s'" % (th.text, p.text))
            continue
        used_ids.append(obj.pk)
    old_ids = all_ids - set(used_ids)
    if old_ids:
        logger.debug("get_ophc_file: Delete %s old ids" % (len(old_ids)))
        OutOfPocketHealthCare.objects.filter(id__in=old_ids).delete()
    # update success
    DocumentStatus.objects.update_or_create(
        document_name=OutOfPocketHealthCare.__name__,
        defaults={'success_time': timezone.now(), 'scheduled': False}
    )
    logger.info("get_ophc_file: Done. Processed %s items" % (len(used_ids)))
    return True


@transaction.atomic
def proceed_transp_file(force=False):
    """ Here in this function we use very complex logic.
        Parsing depends on page structure.
        We assume the structure (and markup) won't change even if the data gets changed.
    """
    SKIPSTATES = "Puerto Rico"
    logger.info("get_transp_file: Start task get_transp_file")
    # get the data
    resp = requests.get(transp_page_url)
    if not resp.ok:
        raise DocParseError("get_transp_file: Cannot retrieve the file: HTTP Code %s: %s"
                            % (resp.status_code, resp.content))
    doc = lxml.html.fromstring(resp.content)
    if not force:
        # check when the page was modified
        transp_docstatus = DocumentStatus.objects.filter(document_name=TransportationStandard.__name__)
        if len(transp_docstatus) > 0:
            transp_docstatus = transp_docstatus[0]
            page_mdf_elem = doc.xpath('//div[@class="modified"]')[0]
            updated_on = transp_updated_re.findall(page_mdf_elem.text)[0]
            updated_on = datetime.datetime.strptime(updated_on, '%d-%b-%Y')
            if transp_docstatus.success_time > updated_on:
                logger.info("get_transp_file: Page was modified on %s but already scanned on %s. Skip processing" %
                            (updated_on.strftime('%d-%m-%Y'), transp_docstatus.success_time.strftime('%d-%m-%Y')))
                return False
    # remember existing IDs to delete those not updated
    all_ids = set(TransportationStandard.objects.all().values_list('id', flat=True))
    used_ids = []

    counties_cache = {}  # {statename_countyname: [(car1, car2), countyid, statename, countyname], ...}
    for county in County.objects.all().values_list('id', 'state_name', 'name'):
        counties_cache["{1}_{2}".format(*county)] = [None] + list(county)
    region_oc, msa_oc = {}, {}  # {name: (car1, car2), ...}
    region_states = {}  # {regionname: [statename1, statename2, ...], ...}

    wy = doc.xpath('//div[@class="wysiwyg"]')[0]  # data container
    maintables = wy.xpath('table/caption/..')  # tables have captions
    ttt_t2k = dict((b, a) for a, b in TRANSPORTATION_TAX_TYPE)  # reverse it to get id by title
    for tbl in maintables:
        maintabletype = None
        for elem in tbl:
            if elem.tag == 'caption':
                caption = elem.text_content()
                maintabletype = ttt_t2k.get(caption)
                if not maintabletype:
                    raise DocParseError(
                        'get_transp_file: Unexpected table structure on the page: unknown caption %s' % (caption))
                logger.debug("get_transp_file: Processing table '%s'" % caption)
                continue
            if elem.tag != 'tr':
                raise DocParseError('get_transp_file: Unexpected table structure on the page: tag %s met' % (elem.tag))
            # processing 'public transportations' table
            if maintabletype == 'publictrans':
                th, td = elem
                if th.tag != 'th' or th.text.strip() != 'National':
                    raise DocParseError(
                        'get_transp_file: Unexpected table (%s) structure on the page: unexpected tag %s with "%s"'
                        % (maintabletype, th.tag, th.text))
                obj, created = TransportationStandard.objects.update_or_create(
                    tax_type=maintabletype, county=None, defaults={
                        'cost_car1': get_num_from_elem(td),
                        'cost_car2': get_num_from_elem(td),
                        'apply_by': 'national',
                    })
                used_ids.append(obj.pk)
            # Processing 'ownership' table
            elif maintabletype == 'ownership':
                th, p1, p2 = elem
                if th.tag == p1.tag == p2.tag == 'th':
                    continue
                if th.tag != 'th' or th.text.strip() != 'National':
                    raise DocParseError(
                        'get_transp_file: Unexpected table (%s) structure on the page: unexpected tag %s with "%s"'
                        % (maintabletype, th.tag, th.text))
                obj, created = TransportationStandard.objects.update_or_create(
                    tax_type=maintabletype, county=None, defaults={
                        'cost_car1': get_num_from_elem(p1),
                        'cost_car2': get_num_from_elem(p2),
                        'apply_by': 'national',
                    })
                used_ids.append(obj.pk)
            # processing 'operating costs' table
            elif maintabletype == 'operating':
                th, p1, p2 = elem
                if th.tag == p1.tag == p2.tag == 'th':
                    continue
                # row contains record either for region or for MSA
                rowname = th.text.strip()
                if rowname.endswith(" Region"):  # row for region
                    rowname = rowname.replace(" Region", "")
                    region_oc[rowname] = (get_num_from_elem(p1), get_num_from_elem(p2))
                    continue
                msa_oc[rowname] = (get_num_from_elem(p1), get_num_from_elem(p2))

    # Here we have 'region_oc' and 'msa_oc' filled with costs
    # We need to find out what states correspond to what MSAs and if not - to what regions

    # Dirty solution warning!
    # We are looking for element "<h3>MSA Definitions by Census Region</h3>" within all children of
    # container element 'wy' (see above). All below will be definitions of regions as a
    # sequence of container tags: p,table,p,table,...

    h3found = False
    for element in wy:
        if element.tag == 'h3':
            h3found = True
            continue
        if not h3found:
            continue
        if element.tag == 'hr':
            break  # final tag
        if element.tag == 'p':  # extract states within region
            mtch = t_region_re.match(element.text_content())
            region, states_st = mtch.groups()
            states = [s.strip() for s in states_st.split(',')]
            region_states[region] = states
        if element.tag == 'table':  # extract counties within MSAs
            cur_msa = None
            for row in element:
                th, td = row
                if td.tag == 'th':
                    continue
                cur_msa = th.text_content().strip() or cur_msa
                if cur_msa not in msa_oc:
                    raise DocParseError("get_transp_file: Unknown msa: %s" % (cur_msa))
                tdtext = td.text_content().strip().replace('’', "'")
                state, counties_st = tdtext.split(':', 1)
                state = state.strip()[-2:]  # was like: "in MA", we need to extract 'MA' only
                state = STATE_CODE2NAME[state]
                for citem in counties_st.split(','):
                    county = citem.strip()
                    ckey = "%s_%s" % (state, county)
                    if ckey not in counties_cache:
                        raise DocParseError("get_transp_file: Unknown state/county pair: %s/%s" % (state, county))
                    # We can use cost for MSA!
                    counties_cache[ckey][0] = msa_oc[cur_msa]

    # finally create/update operating costs
    for costpair, countyid, statename, countyname in counties_cache.values():
        if costpair:
            obj, created = TransportationStandard.objects.update_or_create(
                tax_type='operating', county_id=countyid, defaults={
                    'cost_car1': costpair[0],
                    'cost_car2': costpair[1],
                    'apply_by': 'msa',
                })
            used_ids.append(obj.pk)
        else:
            region = None
            for r, statelist in region_states.items():
                if statename in statelist:
                    region = r
                    break
            else:
                if statename in SKIPSTATES:
                    continue
                raise DocParseError("get_transp_file: Cannot find region for state %s" % (statename))
            # logger.debug("get_transp_file: County %s/%s not found in MSAs, using region %s"
            #              % (statename, countyname, region))
            obj, created = TransportationStandard.objects.update_or_create(
                tax_type='operating', county_id=countyid, defaults={
                    'cost_car1': region_oc[region][0],
                    'cost_car2': region_oc[region][1],
                    'apply_by': 'region',
                })
            used_ids.append(obj.pk)

    # delete old records
    old_ids = all_ids - set(used_ids)
    if old_ids:
        logger.debug("get_transp_file: Delete %s old ids" % (len(old_ids)))
        TransportationStandard.objects.filter(id__in=old_ids).delete()
    # update success
    DocumentStatus.objects.update_or_create(
        document_name=TransportationStandard.__name__,
        defaults={'success_time': timezone.now(), 'scheduled': False}
    )
    logger.info("get_transp_file: Done. Processed %s items" % (len(used_ids)))
    return True


def get_commondoc_file(docklass, runfunc, force=False):
    """ Common file to run proceed_*_file functions from tasks """
    taskname = DOCNAME2TASK[docklass.__name__].__name__
    try:
        if not force:
            obj, created = DocumentStatus.objects.get_or_create(
                document_name=docklass.__name__,
                defaults={'scheduled': False}
            )
            if obj.status == 'error':
                logger.warn("%s: Previous status was error, skip regular run" % (taskname))
                return False
        result = runfunc(force=force)
    except Exception as exc:
        logger.exception("%s error!" % (taskname))
        DocumentStatus.objects.update_or_create(
            document_name=docklass.__name__,
            defaults={'error_time': timezone.now(), 'lasterror': str(exc), 'scheduled': False}
        )
        report_error(docklass)
    return True


@shared_task(name="get_ashs_file")
def get_ashs_file(force=False):
    return get_commondoc_file(HousingUtilitiesStandard, proceed_ashs_file, force)


@shared_task(name="get_fcs_file")
def get_fcs_file(force=False):
    return get_commondoc_file(FoodClothingStandard, proceed_fcs_file, force)


@shared_task(name="get_ophc_file")
def get_ophc_file(force=False):
    return get_commondoc_file(OutOfPocketHealthCare, proceed_ophc_file, force)


@shared_task(name="get_transp_file")
def get_transp_file(force=False):
    return get_commondoc_file(TransportationStandard, proceed_transp_file, force)


DOCNAME2TASK = {
    HousingUtilitiesStandard.__name__: get_ashs_file,
    FoodClothingStandard.__name__: get_fcs_file,
    OutOfPocketHealthCare.__name__: get_ophc_file,
    TransportationStandard.__name__: get_transp_file,
}


def run_update_for(document_name, force=False):
    """ Helper factory function """
    func = DOCNAME2TASK.get(document_name)
    if func:
        func.apply_async(kwargs={'force': force})
        return True
    return False
