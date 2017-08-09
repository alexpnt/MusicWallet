"""
Django settings for musicwalletproject project (Development)
"""

from base import *

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = "q1y1*!a&3v5s-hf7ngbue4(z*@lq*0j!_)q$uw!1#70ot-hn0y"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'musicwallet_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432'
    }
}

