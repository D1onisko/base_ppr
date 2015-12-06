import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ROOT_URLCONF = 'src.urls'

WSGI_APPLICATION = 'src.wsgi.application'

DEBUG = True
TEMPLATE_DEBUG = True
SQL_DEBUG = True

SECRET_KEY = '$)a7n&o80u!6y5t-+jrd3)3!%vh&shg$wqpjpxc!ar&p#!)n1a'

# =====================================================================================================================
#                           DATABASES
# =====================================================================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ppr',
        'USER': 'd1onis',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}
# =====================================================================================================================
#                          LANGUAGE_CODE / TIME_ZONE
# =====================================================================================================================
TIME_ZONE = 'Europe/London'
USE_TZ = True

LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
USE_I18N = True
USE_L10N = True


# ======================================================================================================================
#                               STATIC / MEDIA
# ======================================================================================================================
CRISPY_TEMPLATE_PACK = 'bootstrap3'

MEDIA_ROOT = 'public/media'

MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = 'public/static'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# ======================================================================================================================
#                                 TEMPLATES
# ======================================================================================================================
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
)


# ----------------------------------------------------------------------------------------------------------------------
#                               INSTALLED_APPS / MIDDLEWARE
# ----------------------------------------------------------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    'src.apps.base_ppr',


]


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',


)

# ----------------------------------------------------------------------------------------------------------------------
#                                     MAIL
# ----------------------------------------------------------------------------------------------------------------------
ACCOUNT_ACTIVATION_DAYS = 2

AUTH_USER_EMAIL_UNIQUE = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'info@google.ru'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = (os.path.join(os.path.dirname(__file__), '../mail'))

# ----------------------------------------------------------------------------------------------------------------------
#                                    ElasticSearch
# ----------------------------------------------------------------------------------------------------------------------

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://127.0.0.1:9200/',
        'INDEX_NAME': 'haystack',
    },
}

HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 2
HAYSTACK_CUSTOM_HIGHLIGHTER = 'src.app.search.utils.BorkHighligher'
