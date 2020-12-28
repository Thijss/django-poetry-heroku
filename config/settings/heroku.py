"""Settings for deploying the project to on Heroku"""
# pylint: disable=wildcard-import,unused-wildcard-import,relative-beyond-top-level
import os

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa

# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# HTTPS
# We can safely set this to a high number, since heroku always deploys using https.
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_PRELOAD = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

ALLOWED_HOSTS = ["*"]

# Ensure STATIC_ROOT exists.
os.makedirs(STATIC_ROOT, exist_ok=True)
# Insert Whitenoise Middleware.
MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]
# Enable GZip.
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


if SENTRY_URL := env("SENTRY_URL", ""):
    sentry_sdk.init(
        dsn=SENTRY_URL,
        integrations=[DjangoIntegration()],
        traces_sample_rate=1.0,
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True,
    )

# pylint: disable=fixme
# TODO: When this is set to True, a Value error is thrown (see Sentry)
WHITENOISE_MANIFEST_STRICT = False
