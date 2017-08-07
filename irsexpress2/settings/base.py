# -*- coding: utf-8 -*-

"""
Base Settings
"""
import os
import sys

PROJECT_NAME = 'irsexpress2'

# DEFINE PATHS
PROJECT_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(PROJECT_DIR)
REPO_DIR = os.path.dirname(BASE_DIR)

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# CORE SETTINGS
DEBUG = False
ALLOWED_HOSTS = []
ROOT_URLCONF = 'irsexpress2.urls'
WSGI_APPLICATION = 'irsexpress2.wsgi.application'
AUTH_USER_MODEL = 'user_auth.Account'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

ADMINS = (
    # ('admin', 'admin@localhost'),
)

# APP DECLARATIONS
DJANGO_APPS = (
    # 'admin_tools',
    # 'admin_tools.theming',
    # 'admin_tools.menu',
    # 'admin_tools.dashboard',
    'suit',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
)

THIRD_PARTY_APPS = (
    'crispy_forms',
    'registration',
    'imagekit',
    'storages',
    'localflavor',
)

LOCAL_APPS = (
    'user_auth',
    'utils',
    'landings',
    'clients',
    'repository',
    'irs_common',
    'irs8821',
    'irs433a',
    'irs9465',
    'irs656',
    'agents',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# STATIC AND MEDIA FILES
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'public'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# This would be good to use for file storage, especially user uploads
# DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'

# TEMPLATE_DEBUG = DEBUG
# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
                # 'django.core.context_processors.static',
            ],
        },
    },
]

LOCAL_SETTINGS_FILE = "/usr/local/etc/%s.yaml" % PROJECT_NAME

CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']

# APP SPECFIC SETTINGS
CLIENTS_PAGINATE_BY = 15
CRISPY_TEMPLATE_PACK = 'bootstrap3'
ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = False

# Time when the document will be expired in
# Set to None to disable expiration
# will be applied to new documents only
DOCUMENT_LIFE_TIME = None  # 3600  # seconds
