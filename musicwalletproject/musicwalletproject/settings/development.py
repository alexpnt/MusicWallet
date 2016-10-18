"""
Django settings for musicwalletproject project (Development)
"""

from base import *

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = "q1y1*!a&3v5s-hf7ngbue4(z*@lq*0j!_)q$uw!1#70ot-hn0y"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'musicwallet_db',
        'USER': 'mysql',
        'PASSWORD': 'mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }

}

