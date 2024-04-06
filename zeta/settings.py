#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(override=True)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')
PRODUCTION = bool(os.environ.get('PRODUCTION'))
TELEGRAM_ENDPOINT = os.environ.get("TELEGRAM_ENDPOINT")

PATH_LIST = ['', '/', 'home', 'legal', 'policy', 'error']

if PRODUCTION:

    ALLOWED_HOSTS = ['zeta-pass-nice.org']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    DEBUG = False
    
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'listings.middleware.PermissionDeniedErrorHandler',
    ]

    CSRF_COOKIE_SECURE = True 
    CSRF_TRUSTED_ORIGINS = ['https://zeta-pass-nice.org']
    CSRF_COOKIE_DOMAIN = "zeta-pass-nice.org"
    CSRF_COOKIE_HTTPONLY = True

    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True

else:

    ALLOWED_HOSTS = ['127.0.0.1']
    CSRF_COOKIE_SECURE = True

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

    DEBUG = True

    SESSION_COOKIE_SECURE = True
    LOGIN_URL = 'admin-login'

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'listings.middleware.PermissionDeniedErrorHandler',
    ]

INSTALLED_APPS = [
    'listings',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

ROOT_URLCONF = 'zeta.urls'

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
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'zeta.wsgi.application'

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

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Paris'

USE_I18N = True
USE_TZ = False

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
CSRF_FAILURE_VIEW = 'listings.middleware.errorcsrf'

VERSION = 1.0