from .base import *

DEBUG = False

ALLOWED_HOSTS = ['elsnabukraine.pythonanywhere.com']


INSTALLED_APPS += [
    #  third party apps

    #  local apps
    'home',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'elsnabukraine$elsnab',
        'USER': 'elsnabukraine',
        'PASSWORD': 'adminnimda123abc',
        'HOST': 'elsnabukraine.mysql.pythonanywhere-services.com',
        'PORT': '',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
