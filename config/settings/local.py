# settings/local.py

from .base import *

DEBUG = True

# django-toolbar
# ------------------------------------------------------------------------------
INSTALLED_APPS += ("debug_toolbar", )

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )