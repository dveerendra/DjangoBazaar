# -*- coding: utf-8 -*-

import logging
from bazaar.settings.common import *


##################################################################
# Debug settings
##################################################################

# Set debug
DEBUG = True

# Turns on/off template debug mode.
TEMPLATE_DEBUG = DEBUG

##################################################################
# Databases settings
##################################################################

DATABASES = {
    'test': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SITE_DIR + '/db/testing.sqlite'
    },
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bazaar',
        'USER': 'bazaar',
        'PASSWORD': 'koira',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

##################################################################
# Logging settings
##################################################################

LOG_DATE_FORMAT = '%d %b %Y %H:%M:%S'

LOG_FORMATTER = logging.Formatter(
    u'%(asctime)s | %(levelname)-7s | %(name)s | %(message)s',
    datefmt=LOG_DATE_FORMAT)

CONSOLE_HANDLER = logging.StreamHandler()

CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)

CONSOLE_HANDLER.setLevel(logging.DEBUG)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

##################################################################
# Installed apps
##################################################################

DEVELOPMENT_APPS = (
    # Development specific apps here
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

INSTALLED_APPS = EXTERNAL_APPS + DEVELOPMENT_APPS + INTERNAL_APPS