"""
WSGI config for Karakol project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

import dotenv

from django.core.wsgi import get_wsgi_application

# dotenv settings
dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dot.env')
)


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Karakol.settings')

application=get_wsgi_application()
#os.path.join(os.path.dirname(os.path.dirname(__file__)),
