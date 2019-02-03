import os

PRODUCTION_ENV = 'production'
STAGING_ENV = 'staging'
DEVELOPMENT_ENV = 'development'

if 'ENV' in os.environ and os.environ['ENV'] in [PRODUCTION_ENV, STAGING_ENV, DEVELOPMENT_ENV]:
    env_type = os.environ['ENV']
    if env_type.lower() == PRODUCTION_ENV:
        from .production import *
        CURRENT_ENV = PRODUCTION_ENV
    elif env_type.lower() == STAGING_ENV:
        from .staging import *
        CURRENT_ENV = STAGING_ENV
    elif env_type.lower() == DEVELOPMENT_ENV:
        from .dev import *
        CURRENT_ENV = DEVELOPMENT_ENV
else:
    if os.path.exists(os.path.join(os.getcwd(), '..', 'DEVELOPMENT')):
        from .dev import *  # noqa
        CURRENT_ENV = DEVELOPMENT_ENV
    elif os.path.exists(os.path.join(os.getcwd(), '..', 'STAGING')):
        from .staging import *  # noqa
        CURRENT_ENV = STAGING_ENV
    else:
        from .production import *  # noqa
        CURRENT_ENV = PRODUCTION_ENV
