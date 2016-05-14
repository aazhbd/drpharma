import os

os.environ['HTTP_HOST'] = 'drpharma.articulatelogic.com'

from . __init__ import * #@UnusedWildImport

DATABASES['default']['USER'] = ''
DATABASES['default']['PASSWORD'] = ''

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
