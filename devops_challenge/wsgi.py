import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops_challenge.settings")

application = get_wsgi_application()
