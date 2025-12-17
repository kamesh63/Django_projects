"""
WSGI config for django_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

wsgi.py	configures	a	WSGI	(Web	Server	Gateway	Interface)	application,
the	default	setting	for	Django

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")

application = get_wsgi_application()
