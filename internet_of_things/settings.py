# -*- coding: utf-8 -*-
"""
Django settings for internet_of_things project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

USE_I18N = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*#18z+=iwx7yxi3&mzxz0c9bnah#h!u%1j+4y6+hc!10t1ncd#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

# For Sidebar Menu (List of apps and models) (RECOMMENDED)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)
BOOTSTRAP_ADMIN_SIDEBAR_MENU = True


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    #'bootstrap_admin', # always before django.contrib.admin
    #'django.contrib.admin',
    'material',
    'material.frontend',
    #'easy_pjax',
    'material.admin',
    'admin_reorder',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'iot',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'audit_log.middleware.UserLoggingMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
)

ROOT_URLCONF = 'internet_of_things.urls'


TEMPLATE_DIRS = (
     BASE_DIR + '/templates/',
)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [#'/var/www/material/InternetOfThings_material/templates',
		'/var/www/material/InternetOfThings_material/material/admin/templates/',
		 '/var/www/material/InternetOfThings_material/material/templates/',
		 '/var/www/material/lib/python2.7/site-packages/django/contrib/admin/templates'
		],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                #'material.frontend.context_processors.modules',
            ],
        },
    },
]


ADMIN_REORDER = (
    # Keep original label and models
    'sites',

    # Rename app
    #{'app': 'auth', 'label': 'Contas de Utilizadores'},

    # Reorder app models
    {'app': 'auth', 'models': ('auth.User', 'auth.Group')},
    {'app': 'iot', 'models': ('iot.Template', 'iot.Equipment', 'iot.Sensor', 'iot.Parameter')},

    # Exclude models
    #{'app': 'auth', 'models': ('auth.User', )},

    # Cross-linked models
    #{'app': 'auth', 'models': ('auth.User', 'sites.Site')},

    # models with custom name
    #{'app': 'auth', 'models': (
     #   'auth.Group',
    #    {'model': 'auth.User', 'label': 'Staff'},
    #)},
)

ROOT_URLCONF = 'internet_of_things.urls'

WSGI_APPLICATION = 'internet_of_things.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'iot',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': '127.0.0.1',  # Or an IP Address that your DB is hosted on
        'PORT': '',
    }
}


# ESQUEMA DE LOGIN
AUTH_PROFILE_MODULE = 'InternetOfThings.login'
LOGIN_URL = '/InternetOfThings/login'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt_PT'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

LANGUAGES = (
    ('pt_PT', u'Portugues'),
    #('en', u'Ingles'),
)


TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "iot")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
#MEDIA_URL = 'http://192.168.5.82:8002/static/'
MEDIA_URL = 'http://127.0.0.1:8000/static/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
#STATIC_ROOT = '/home/Gestsport/opt/GestVisitor_0_1/gestvisitor/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, "static/")
STATIC_ROOT = "/var/www/material/InternetOfThings_material/iot/static/"
#DIR_IMPORT = "/home/Gestsport/opt/GestVisitor_0_1/import/"

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'


import django.contrib.auth
django.contrib.auth.LOGIN_URL = '/'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
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


LOGIN_REDIRECT_URL = '/'


