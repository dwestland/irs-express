# -*- coding: utf-8 -*-

DESCRIPTION = """
    Script file pdfform_extract

    Converts PDF Form to YAML file with the list of fields.
    Uses pdftk tool (should be installed).

    Author: Alexey Kolyanov, 2015

"""


import os
import sys
import yaml
from operator import itemgetter
from collections import defaultdict
import logging

from django.core.management.base import BaseCommand, CommandError

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = (DESCRIPTION)

    def add_arguments(self, parser):
        parser.add_argument('-i', '--inputfile', help='Input file', required=True)
        parser.add_argument('-o', '--outputfile', help='Output YAML file', required=True)

    def handle(self, *args, **options):
        if not os.path.exists(options.get('inputfile')):
            raise CommandError("Input file %s does not exist!" % options.get('inputfile'))

        tmpfile = "/tmp/_pdfform_extract.txt"
        pdfdata = ""
        try:
            cmd = 'pdftk "{src}" dump_data_fields_utf8 > {tmpfile}'.\
                format(src=options.get('inputfile'), tmpfile=tmpfile)
            retcode = os.system(cmd)
            if retcode != 0:
                raise Exception("Error executing command dump_data_fields_utf8: code %s" % retcode)
            with open(tmpfile, 'r') as tf:
                pdfdata = tf.read()
        except Exception as ee:
            raise CommandError("Error %s: %s" % (type(ee), str(ee)))
        finally:
            if os.path.exists(tmpfile):
                os.unlink(tmpfile)

        item_cnt = 0
        known_fields = ['FieldType', 'FieldName', 'FieldNameAlt', 'FieldFlags',
                        'FieldJustification', 'FieldMaxLength', 'FieldValue', 'FieldValueDefault']
        all_elements = []
        fieldtypes = defaultdict(int)
        cur_element = {}
        prev_field = ""
        for line in pdfdata.split("\n"):
            if line == '---':
                if cur_element:
                    all_elements.append(cur_element)
                    cur_element = {}
                item_cnt += 1
                prev_field = ""
                continue
            if not any(line.startswith("%s: " % f) for f in known_fields):
                if prev_field:
                    # print(line)
                    # print(prev_field)
                    cur_element[prev_field] += line
                continue
            fieldname, content = line.split(': ', 1)
            if fieldname in ('FieldMaxLength', 'FieldFlags'):
                content = int(content)
            if fieldname == 'FieldType':
                fieldtypes[content] += 1
            cur_element[fieldname] = content
            prev_field = fieldname
        if cur_element:
            all_elements.append(cur_element)

        all_elements = sorted(all_elements, key=itemgetter('FieldName'))

        with open(options.get('outputfile'), 'w') as outf:
            outf.write(yaml.safe_dump(all_elements, allow_unicode=True, indent=4, default_flow_style=False))

        print("Processed %s items" % item_cnt)
        print("Field types: %s" % set(fieldtypes.items()))
