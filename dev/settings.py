# Include all global variables in this file.
# These are used across different modules/packages
# where required.

# Service Name
SVC_NAME = 'batman-ms-pagerduty'

# DB Settings
DB_HOST_WRITER = '127.0.0.1'
DB_HOST_READER = '127.0.0.1'
DB_PORT = 3306
DB_NAME = 'batman_pagerduty'
DB_USER = 'root'
DB_PASS = ''

# Pagerduty Settings
PAGERDUTY_API = 'https://api.pagerduty.com'
PAGERDUTY_TOKEN = ''
PAGERDUTY_BATMAN_TEAMID = ''
PAGERDUTY_BATMAN_SCHEDULEID = ''

# Sentry Settings
SENTRY_DSN = ''
SENTRY_TRACES_SAMPLE_RATE = 1.0
SENTRY_PROFILES_SAMPLE_RATE = 1.0
SENTRY_ENV = 'development'

# Flask Settings
FLASK_PORT = 80
FLASK_DEBUG = True