"""Settings for deploying the project to on Heroku"""
# pylint: disable=wildcard-import,unused-wildcard-import,relative-beyond-top-level
import django_heroku

from .base import *

# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# HTTPS
# We can safely set this to a high number, since heroku always deploys using https.
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

django_heroku.settings(locals())
