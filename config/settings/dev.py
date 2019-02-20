from .base import *  # noqa

DEBUG = True

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = 'media'

MEDIA_URL = '/media/'

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config.get('email', 'HOST')
EMAIL_HOST_USER = config.get('email', 'USER')
EMAIL_HOST_PASSWORD = config.get('email', 'PASSWORD')
EMAIL_PORT = config.get('email', 'PORT')
EMAIL_USE_TLS = config.getboolean('email', 'USE_TLS')
DEFAULT_FROM_EMAIL = config.get('email', 'DEFAULT_FROM_EMAIL')
EMAIL_FROM = config.get('email', 'EMAIL_FROM')
EMAIL_SUBJECT_PREFIX = '[RyderSportAcademy] '

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
