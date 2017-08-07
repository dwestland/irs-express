# -*- coding: utf-8 -*-

LOG_FOLDER = "/var/log/irsexpress2"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FOLDER + '/webdebug.log',
            'formatter': 'verbose',
        },
        'repotasks_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FOLDER + '/tasks_repository.log',
            'formatter': 'verbose',
        },
        'irs_tasks_file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': LOG_FOLDER + '/tasks_irs.log',
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', ],
            'level': 'ERROR',
            'propagate': True,
        },
        'main': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'repository.tasks': {
            'handlers': ['repotasks_file', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'irs433a.tasks': {
            'handlers': ['irs_tasks_file', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'irs656.tasks': {
            'handlers': ['irs_tasks_file', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'irs8821.tasks': {
            'handlers': ['irs_tasks_file', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'irs9465.tasks': {
            'handlers': ['irs_tasks_file', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'irs_common.tasks': {
            'handlers': ['irs_tasks_file', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        # default loggers per-app
        'irs_common': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'clients': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'utils': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'irs433a': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'irs656': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'iri8821': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'irs9465': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'repository': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'user_auth': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
        'agents': {
            'handlers': ['file', ],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
