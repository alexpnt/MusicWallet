import os
import sys

path = '/home/musicwallet/MusicWallet/musicwalletproject'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'musicwalletproject.settings.production'
os.environ['SECRET_KEY'] = 'q1y1*!a&3v5s-hf7ngbue4(z*@lq*0j!_)q$uw!1#70ot-hn0y'
os.environ['DB_USER'] = 'musicwallet'
os.environ['DB_PASSWORD'] = 'mysqldatabase'

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())