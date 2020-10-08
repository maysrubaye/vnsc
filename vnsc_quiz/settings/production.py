from __future__ import absolute_import, unicode_literals
from .base import *
import dj_database_url

DEBUG = True

import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/vnsc_quiz')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))


env = os.environ.copy()
SECRET_KEY = os.getenv('SECRET_KEY')



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'



DATABASES['default'] =  dj_database_url.config()
    
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']


try:
    from .local import *
except ImportError:
    pass

