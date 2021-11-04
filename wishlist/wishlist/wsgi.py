"""
WSGI config for wishlist project.
web server gateway interface(actual server)
It exposes the WSGI callable as a module-level variable named ``application``.

"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wishlist.settings')

application = get_wsgi_application()
