"""
WSGI config for django_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
"""

import os

from django.core.wsgi import get_wsgi_application

<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_blog.settings")
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_blog.settings')
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3

application = get_wsgi_application()
