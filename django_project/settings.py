# -- coding: utf-8 --"
"""
Django settings for project project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8y_gdfj^aaqgwwi6n8g#w42pfdqa*6p7u%q(252b@j_0o7cv9c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SITE_ID = 1
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['localhost']
LOGIN_URL = '/auth/login/'
# DEFAULT_HOST = 'index'
# ROOT_HOSTCONF = 'project.hosts'
# Application definition
AUTHENTICATION_BACKENDS = (
    'myauth.auth_backends.CustomUserModelBackend',
)
CUSTOM_USER_MODEL = 'myauth.UserProfile'
SESSION_COOKIE_DOMAIN = '.ondrive.loc'
SESSION_COOKIE_NAME = 'ondrivesession'

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'news',
    'tuning',
    'service',
    'ckeditor',
    'sitetree',
    'myauth',
    'reviews',
    'contacts',
    'pages',
    'htmlblock',
    'rest_framework',
    'django_hosts'
)
MIDDLEWARE_CLASSES = (
    'django_hosts.middleware.HostsRequestMiddleware',
    'django_hosts.middleware.HostsResponseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_project.urls'
ROOT_HOSTCONF = 'django_project.hosts'
WSGI_APPLICATION = 'django_project.wsgi.application'
DEFAULT_HOST = 'default'
PARENT_HOST = 'ondrive.loc'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'django.core.context_processors.media',
)
TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates',
)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
#STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','static'))

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_PATH + '/static',
)
#STATIC_ROOT = PROJECT_PATH + '/static'

# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder'
# )

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','media'))


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'width': '100%',
    },
}

CKEDITOR_UPLOAD_PATH = "upload/content/"


DISQUS_SECRET_KEY = 'gUE2zeP5jaMXf1D4YnaoiKRMyrLMf7oImKuNDh78QYafULtC2CMvM6pCe4mflJoc'
DISQUS_PUBLIC_KEY = 'oCdxoSVB6daOfXK5oQWT2RBsbXnM1fd37nZkmBdq8WJiMPiafJ2i6n5fERvg7ESO'

EMAIL_HOST = 'smtp.fullspace.ru'
EMAIL_HOST_USER = 'info@ondrive.by'
EMAIL_HOST_PASSWORD = 'on89drive'
EMAIL_PORT = 465
EMAIL_USE_SSL = True


REST_FRAMEWORK = {
    'PAGINATE_BY': 500,                 # Default to 10
    'PAGINATE_BY_PARAM': 'pageSize',  # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100             # Maximum limit allowed when using `?page_size=xxx`.
}




