# -*- coding: utf-8 -*-

from __future__ import absolute_import

import os
import sys
import gc

from celery import Celery
from celery.signals import task_postrun

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'irsexpress2.settings')

app = Celery('irsexpress2')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.LOCAL_APPS)


# See https://groups.google.com/d/msg/celery-users/jVc3I3kPtlw/fPfnoP_DhuoJ
@task_postrun.connect
def collect_after_task(**kwargs):
    gc.collect()
