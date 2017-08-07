# -*- coding: utf-8 -*-

import sys
import os
import logging

from celery import shared_task

from .models import Client, ClientDocument

logger = logging.getLogger(__name__)


@shared_task(name="delete_document")
def delete_document(document_id: int):
    logger.info("Start task: delete document %s" % document_id)
    try:
        if ClientDocument.objects.filter(id=document_id).exists():
            doc = ClientDocument.objects.get(pk=document_id)
            doc.delete()
        logger.info("Start document %s deleted" % document_id)
    except:
        logger.exception("Error while deleting document %s!" % document_id)


@shared_task(name="delete_client")
def delete_client(client_id: int):
    c = Client.objects.get(pk=client_id)
    c.delete()
