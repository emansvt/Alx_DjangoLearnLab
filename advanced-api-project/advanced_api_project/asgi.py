"""
ASGI config for advanced_api_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "advanced_api_project.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3

application = get_asgi_application()
