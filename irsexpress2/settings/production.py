"""
Production Settings
"""
from .base import *

APPS = ()

INSTALLED_APPS += APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
}

BROKER_URL = 'sqla+sqlite:///%s' % os.path.join(BASE_DIR, 'celery_brokerdb.sqlite')
CELERY_RESULT_BACKEND = 'db+sqlite:///%s' % os.path.join(BASE_DIR, 'celery_resultsdb.sqlite')

# Email settings used for email sending
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''  # 'smtp.server.name'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = ''
SERVER_EMAIL = ''  # put your account name
