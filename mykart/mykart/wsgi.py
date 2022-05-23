from email.mime import application
import os

from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE','mykart.settings')
application=get_wsgi_application()
