"""
Django settings for turing project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import environ

# Conf
ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path('turing')
ENV_PATH = str(APPS_DIR.path('.env'))

env = environ.Env()
if env.bool('READ_ENVFILE', default=True):
    env.read_env(ENV_PATH)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='r((ws^80$x*0sm6wdvqgi&l@eea^f@%!+9%ah35gcas6oukgj#')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', True)

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=['localhost'])


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'public.apps.PublicConfig',
    'contributor.apps.ContributorConfig',
    'algorun.apps.AlgorunConfig',
    'algopiper.apps.AlgopiperConfig',
    'corsheaders'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'turing.urls'

CORS_ORIGIN_ALLOW_ALL = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'turing.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASE_URL = 'sqlite:///db.sqlite3'
POSTGRES_HOST = env('POSTGRES_HOST', default=None)
POSTGRES_DB = env('POSTGRES_DB', default=None)
POSTGRES_USER = env('POSTGRES_USER', default=None)
POSTGRES_PASSWORD = env('POSTGRES_PASSWORD', default=None)
if POSTGRES_DB and POSTGRES_USER and POSTGRES_PASSWORD and POSTGRES_HOST:
    DATABASE_URL = 'postgres://' + POSTGRES_USER + ':' + POSTGRES_PASSWORD + '@' + POSTGRES_HOST + '/' + POSTGRES_DB

DATABASES = {
    'default': env.db('DATABASE_URL', default=DATABASE_URL),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
DATABASES['default']['CONN_MAX_AGE'] = 600


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

APPEND_SLASH=False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", default=str(APPS_DIR.path('assets')))

ALGOMANAGER = env('ALGOMANAGER', default='http://localhost:8000/algopiper') 
SERVER_PATH = env('SERVER_PATH', default='http://localhost')