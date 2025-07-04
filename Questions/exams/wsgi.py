"""
WSGI config for exams project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

# Caminho onde está o diretório 'exams'
path = '/home/alexdeitos/ProvaMySQL2/Questions'
if path not in sys.path:
    sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exams.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

