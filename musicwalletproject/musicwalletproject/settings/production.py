"""
Django settings for musicwalletproject project (Production)
"""

from base import *

DEBUG = True

# ALLOWED_HOSTS = ['*']

SECRET_KEY = "q1y1*!a&3v5s-hf7ngbue4(z*@lq*0j!_)q$uw!1#70ot-hn0y"

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'musicwallet$musicwallet_db',
        'USER': "musicwallet",
        'PASSWORD': "mysqldatabase",
        'HOST': 'musicwallet.mysql.pythonanywhere-services.com',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )