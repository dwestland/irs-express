# -*- coding: utf-8 -*-

import logging

from django.core.management.base import BaseCommand, CommandError

from irs8821.tasks import fill_form_8821

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = ('Update IRS Local and National Standards Tables')

    def add_arguments(self, parser):
        parser.add_argument('--sync', action='store_true', help='Run it synchronously')
        parser.add_argument('--client_id', help='Client ID', required=True)
        parser.add_argument('--outfile', help='Output PDF file')

    def handle(self, *args, **options):
        sync = options.get('sync') or False
        if sync:
            fill_form_8821(client_id=options.get('client_id'), outfile=options.get('outfile'))
        else:
            fill_form_8821.apply_async(kwargs={'client_id': options.get('client_id'),
                                               'outfile': options.get('outfile')})
