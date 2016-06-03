from .base import *

DEBUG = False

SECRET_KEY = get_secret("SECRET_KEY")

########## AWS SETTINGS
AWS_ACCESS_KEY_ID = get_secret("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_secret("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = get_secret("AWS_STORAGE_BUCKET_NAME")
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
AWS_PRELOAD_METADATA = True

AWS_EXPIREY = 60 * 60 * 24 * 7
AWS_HEADERS = {
    'Cache-Control': 'max-age=%d, s-maxage=%d, must-revalidate' % (AWS_EXPIREY, AWS_EXPIREY)
}
######### END AWS SETTINGS

######### STATIC SETTINGS
STATIC_URL = "https://s3.amazonaws.com/%s/" % AWS_STORAGE_BUCKET_NAME
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
######### END STATIC SETTINGS

########## EMAIL CONFIGURATION
EMAIL_BACKEND = 'django_ses.SESBackend'
# Additionally, you can specify an optional region, like so:
AWS_SES_REGION_NAME = 'eu-west-1'
AWS_SES_REGION_ENDPOINT = 'email.eu-west-1.amazonaws.com'
SERVER_EMAIL = 'carl.bednorz@de.soliver.com'
########## END EMAIL CONFIGURATION

########## CACHE CONFIGURATION
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
########## END CACHE CONFIG

########## LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'django': {
            'format':'django: %(message)s',
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose'
        },
        'logging.handlers.SysLogHandler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'facility': 'local7',
            'formatter': 'django',
            'address' : '/dev/log',
           },
    },
    'loggers': {
        'django': {
            'handlers':['null'],
            'propagate': True,
            'level':'ERROR',
        },
        'django.request': {
            'handlers': ['logging.handlers.SysLogHandler'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security.DisallowedHost': {
            'handlers': ['logging.handlers.SysLogHandler'],
            'propagate': False,
        },
        'backlogr': {
            'handlers': ['logging.handlers.SysLogHandler'],
            'propagate': True,
            'level': 'INFO',
        },
        'loggly_logs':{
             'handlers': ['logging.handlers.SysLogHandler'],
             'propagate': True,
             'format':'django: %(message)s',
             'level': 'DEBUG',
           },
    }
}
####### END LOGGING
