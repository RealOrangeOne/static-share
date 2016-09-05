import dj_database_url
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', True)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'flat',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'admin_resumable',
    'shortuuidfield',

    'project.files',
    'project.pages'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware'
)

ROOT_URLCONF = 'project.urls'

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
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

if 'OPBEAT_SECRET_TOKEN' in os.environ and 'IN_TEST' not in os.environ:
    OPBEAT = {
        'ORGANIZATION_ID': os.environ['OPBEAT_ORGANIZATION_ID'],
        'APP_ID': os.environ['OPBEAT_APP_ID'],
        'SECRET_TOKEN': os.environ['OPBEAT_SECRET_TOKEN'],
    }

    MIDDLEWARE_CLASSES = (
        'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    ) + MIDDLEWARE_CLASSES

    INSTALLED_APPS = (
        "opbeat.contrib.django",
    ) + INSTALLED_APPS


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default=os.environ['DATABASE_URL'])
}

EMAIL_BACKEND = os.environ['EMAIL_BACKEND']


LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'request_id': {
            '()': 'log_request_id.filters.RequestIDFilter'
        }
    },
    'formatters': {
        'standard': {
            'format': 'at=%(levelname)s request_id=%(request_id)s logger=%(name)s %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'filters': ['request_id'],
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
        'log_request_id.middleware': {
            'level': 'INFO',
            'propagate': True,
        },
        'project': {
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

if 'IN_TEST' in os.environ:
    logging.disable(logging.ERROR)


STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'collected-static')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static', 'build'),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ADMIN_RESUMABLE_SHOW_THUMB = True
ADMIN_RESUMABLE_SUBDIR = 'uploads'
MEDIA_URL = '/'
