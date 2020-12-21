"""Settings for running the project in a local environment."""
# pylint: disable=wildcard-import,unused-wildcard-import,relative-beyond-top-level
from .base import *  # noqa

ALLOWED_HOSTS = []

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
