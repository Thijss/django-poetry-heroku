"""Settings for deploying the project to on Heroku"""
# pylint: disable=wildcard-import,unused-wildcard-import,relative-beyond-top-level
import django_heroku

from .base import *

# TODO: Add settings from Django's deployment checklist
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

django_heroku.settings(locals())
