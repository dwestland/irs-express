# -*- coding: utf-8 -*-

import logging

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from repository.tasks import get_ashs_file, get_fcs_file, get_ophc_file, get_transp_file

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = ('Update IRS Local and National Standards Tables')
    option_list = BaseCommand.option_list + (
        make_option('--sync', action='store_true', help='Run it synchronously'),

        make_option('--ashs', action='store_true', help='Run only for all_states_housing_standards'),
        make_option('--fcs', action='store_true', help='Run only for Food, Clothing and Other Items Standards'),
        make_option('--ophc', action='store_true', help='Run only for Out-of-Pocket Health Care Standards'),
        make_option('--transp', action='store_true', help='Run only for Transportation Standards'),
    )

    def handle(self, *args, **options):
        sync = options.get('sync') or False
        run_all = all(not options.get(tn) for tn in ('ashs', 'fcs', 'ophc', 'transp'))
        if sync:
            if run_all or options.get('ashs'):
                get_ashs_file(force=True)
            if run_all or options.get('fcs'):
                get_fcs_file(force=True)
            if run_all or options.get('ophc'):
                get_ophc_file(force=True)
            if run_all or options.get('transp'):
                get_transp_file(force=True)
        else:
            if run_all or options.get('ashs'):
                logger.info("Start task to get all_states_housing_standards.pdf")
                get_ashs_file.apply_async(kwargs={'force': True})
            if run_all or options.get('fcs'):
                logger.info("Start task to get Food, Clothing and Other Items Standards")
                get_fcs_file.apply_async(kwargs={'force': True})
            if run_all or options.get('ophc'):
                logger.info("Start task to get Out-of-Pocket Health Care Standards")
                get_ophc_file.apply_async(kwargs={'force': True})
            if run_all or options.get('transp'):
                logger.info("Start task to get Allowable Living Expense Transportation Standards")
                get_transp_file.apply_async(kwargs={'force': True})
