# -*- coding: utf-8 -*-

import sys
import os
import yaml
import time
import logging

from django.shortcuts import render
from django.template import Context, Template

from celery import shared_task

from .utils import generate_xfdf

logger = logging.getLogger(__name__)

CUR_DIR = os.path.dirname(os.path.abspath(__file__))


@shared_task(name="mytask")
def mytask():
    pass


def fill_pdf_form(source_pdf: 'str, Path to source PDF file',
                  fields_yaml_path: 'str, Path to formname.yaml.tpl file with fields descriptions',
                  context: 'dict, context variables',
                  return_value: 'Boolean, Whether this function should return data (True) or just fill outfile' = False,
                  outfile: 'str, Path to resulting PDF file to be created' = None
                  ):
    tmp_id = int(time.time())
    context = Context(context)
    with open(fields_yaml_path, 'r') as yf:
        tpl = Template(yf.read())
        ydata_raw = tpl.render(context=context)
    ydata = ""
    # a bit escape the lines
    for line in ydata_raw.split("\n"):
        if not line.startswith('    value:'):
            ydata += line + "\n"
            continue
        _, value = line.split(': ', 1)
        value = value.replace('"', '\\"')
        ydata += '    value: "' + value + '"' + "\n"
    # load as yaml
    # with open('/tmp/_yaml_%s.yaml' % tmp_id, 'w') as yf:
    #     yf.write(ydata)
    # return False
    allfields = yaml.load(ydata)
    fdf_data = []
    field_with_values, total_fields = 0, 0
    # loop over all fields
    for fdesc in allfields:
        value = None
        ftype = fdesc['FieldType']
        if ftype == '':  # markup element
            continue
        total_fields += 1
        fname = fdesc['FieldName']
        maxlen = fdesc.get('FieldMaxLength') or sys.maxsize
        default = fdesc.get('default') or "N/A"
        if 'value' in fdesc:
            value = fdesc.get('value')
            field_with_values += 1
            # logger.debug("Field %s: (%s) %s" % (fname, type(value), value))
        else:
            pass
            # value = fname
            # logger.warn("Field %s has no value!" % (fname))

        if ftype == 'Text':
            value = str(value or '').strip()
            if not value:
                value = default
            if value == '--empty--':
                value = ''
            value = str(value)[:maxlen]
        fdf_data.append((fname, value))
    logger.debug("%s/%s fields processed" % (field_with_values, total_fields))

    # generate Xfdf
    tmpfdffile = "/tmp/_%s_form.xfdf" % tmp_id
    tmpoutfile = "/tmp/_pdf_%s_form.pdf" % tmp_id
    if not outfile:
        outfile = tmpoutfile
    try:
        xfdf = generate_xfdf(fdf_data)
        with open(tmpfdffile, 'wb') as fdff:
            fdff.write(xfdf)
        cmd = "pdftk {inputfile} fill_form {fdffile} output {outputfile} flatten > /dev/null 2>&1"
        cmd = cmd.format(inputfile=source_pdf, fdffile=tmpfdffile, outputfile=outfile)
        logger.debug("Call: %s" % cmd)
        retval = os.system(cmd)
        if retval != 0:
            raise Exception("system() call failed with code %s" % retval)
        logger.debug("Resulting PDF: %s" % outfile)
        if return_value:
            with open(outfile, 'rb') as rpdf:
                return rpdf.read()
    except:
        logger.exception("FDF processing error")
    finally:
        for rmfile in (tmpfdffile, tmpoutfile):
            if os.path.exists(rmfile):
                # pass
                os.unlink(rmfile)
