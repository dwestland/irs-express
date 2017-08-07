# -*- coding: utf-8 -*-

import sys
import os
import yaml
import logging

from celery import shared_task

from irs_common.tasks import fill_pdf_form
from clients.models import Client

logger = logging.getLogger(__name__)

CUR_DIR = os.path.dirname(os.path.abspath(__file__))

SOURCE_PDF = os.path.join(CUR_DIR, 'pdfdata', 'f9465.pdf')
FIELDS_YAML_FILE = os.path.join(CUR_DIR, 'pdfdata', 'f9465.yaml.tpl')


@shared_task(name="fill_form_9465")
def fill_form_9465(client_id: int, return_value=False, outfile=None):
    client = Client.objects.get(id=client_id)
    form = client.get_form_9465()
    context = {
        'form': form, 'client': client
    }
    result = fill_pdf_form(SOURCE_PDF, FIELDS_YAML_FILE, context, return_value, outfile)
    return result
