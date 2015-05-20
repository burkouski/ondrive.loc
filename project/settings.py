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

# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'news',
    'tuning',
    'service',
    'ckeditor',
    'sitetree',
    'myauth',
    'reviews',
    'contacts',
    'pages',
    'htmlblock'
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'project.urls'
AJAX_CRAWLING_URLCONF = 'project.urls_ajax_crawling'
WSGI_APPLICATION = 'project.wsgi.application'


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

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..','media'))


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
}

CKEDITOR_UPLOAD_PATH = "upload/"


DISQUS_SECRET_KEY = 'gUE2zeP5jaMXf1D4YnaoiKRMyrLMf7oImKuNDh78QYafULtC2CMvM6pCe4mflJoc'
DISQUS_PUBLIC_KEY = 'oCdxoSVB6daOfXK5oQWT2RBsbXnM1fd37nZkmBdq8WJiMPiafJ2i6n5fERvg7ESO'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ondrive.by@gmail.com'
EMAIL_HOST_PASSWORD = '27b02v89s'
EMAIL_PORT = 587




