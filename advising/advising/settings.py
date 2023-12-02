"""
Django settings for advising project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from configurations import Configuration
from dotenv import load_dotenv

load_dotenv()
import os

# import templates.BASE_DIR
import dj_database_url


"""
class Dev(Configuration):
    BASE_DIR = Path(__file__).resolve().parent.parent
    SECRET_KEY = str(os.getenv('SECRET_KEY'))
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']
    #CommandError: You must set settings.ALLOWED_HOSTS if DEBUG is False., even with ['*']

https://syntaxfix.com/question/8315/commanderror-you-must-set-settings-allowed-hosts-if-debug-is-false



For Windows:
If you're using Powershell, the command should be $env:DJANGO_SETTINGS_MODULE= 'your_value'.
If you're using batch (aka "cmd"), it's set DJANGO_SETTINGS_MODULE="your_value"


"""
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv("SECRET_KEY"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "checklist.adminconfig.ChecklistAdminConfig",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "checklist",
    "debug_toolbar",
    "crispy_forms",
    "crispy_bootstrap5",
    "import_export",
]

# SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "advising.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

WSGI_APPLICATION = "advising.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    "default": dj_database_url.config(default=f"sqlite:///{BASE_DIR}/db.sqlite3")
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# cache
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:8000",
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "/static/"

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

STATIC_ROOT = os.path.join(BASE_DIR, "static_production_test")

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

#fixtures
FIXTURE_DIRS = [os.path.join(BASE_DIR, "fixtures")]


# media

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


INTERNAL_IPS = ["127.0.0.1"]

# crispy
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


# import export
from import_export.formats.base_formats import CSV, XLSX

IMPORT_FORMATS = [CSV, XLSX]
EXPORT_FORMATS = [CSV, XLSX]

"""
class Prod(Dev):
    DEBUG = False
    SECRET_KEY =  str(os.getenv('SECRET_KEY'))
    #SECRET_KEY = values.SecretValue()
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']

"""

# python manage.py diffsettings --all

