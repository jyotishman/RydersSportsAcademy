import logging
from .base import *  # noqa

DEBUG = False

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# AWS S3 credentials used for media
AWS_ACCESS_KEY_ID = config.get('s3', 'AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config.get('s3', 'AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config.get('s3', 'AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_CUSTOM_DOMAIN = config.get('s3', 'AWS_S3_CUSTOM_DOMAIN', fallback=AWS_S3_CUSTOM_DOMAIN)
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_S3_USE_SSL = config.getboolean('s3', 'AWS_S3_USE_SSL', fallback=False)

MEDIA_ROOT = 'media'

MEDIA_URL = '%s://%s/%s/' % ('https' if AWS_S3_USE_SSL else 'http', AWS_S3_CUSTOM_DOMAIN, MEDIA_ROOT)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config.get('email', 'HOST')
EMAIL_PORT = config.get('email', 'PORT')
EMAIL_USE_TLS = config.getboolean('email', 'USE_TLS')
DEFAULT_FROM_EMAIL = config.get('email', 'DEFAULT_FROM_EMAIL')

SENTRY_DSN = config.get('sentry', 'DSN', fallback=None)
if SENTRY_DSN:
    # raven sentry client
    # See https://docs.sentry.io/clients/python/integrations/django/
    INSTALLED_APPS += ['raven.contrib.django.raven_compat', ]
    RAVEN_MIDDLEWARE = ['raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware']
    MIDDLEWARE = RAVEN_MIDDLEWARE + MIDDLEWARE

    SENTRY_CLIENT = 'raven.contrib.django.raven_compat.DjangoClient'

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'root': {
            'level': 'WARNING',
            'handlers': ['sentry'],
        },
        'formatters': {
            'verbose': {
                'format': '%(levelname)s  %(asctime)s  %(module)s '
                          '%(process)d  %(thread)d  %(message)s'
            },
        },
        'handlers': {
            'sentry': {
                'level': 'ERROR',  # To capture more than ERROR, change to WARNING, INFO, etc.
                'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
                'tags': {'custom-tag': 'x'},
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db.backends': {
                'level': 'ERROR',
                'handlers': ['console'],
                'propagate': False,
            },
            'raven': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'sentry.errors': {
                'level': 'DEBUG',
                'handlers': ['console'],
                'propagate': False,
            },
            'django.security.DisallowedHost': {
                'level': 'ERROR',
                'handlers': ['console', 'sentry', ],
                'propagate': False,
            },
        },
    }
    SENTRY_CELERY_LOGLEVEL = logging.INFO
    RAVEN_CONFIG = {
        'CELERY_LOGLEVEL': logging.INFO,
        'DSN': SENTRY_DSN
    }