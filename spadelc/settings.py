"""
Django settings for spadelc project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

#from pathlib import Path

import os
from decouple import config

# import locale


# import django
# from django.utils.encoding import smart_str
# django.utils.encoding.smart_text = smart_str

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-d6u-y*_emvopwe+qqg!y^le8k*0=facyw9t4hev_ed1u80j!d9'
SECRET_KEY = config('SECRET_KEY')
# http://localhost:8000/
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# python manage.py runserver 192.168.1.52:8000
ALLOWED_HOSTS = [
    # '10.0.2.2',
    '192.168.1.52',
    # '192.168.1.15',
    'localhost',
    # '10.0.3.2',
    '127.0.0.1',
    "chrome-extension://eejfoncpjfgmeleakejdcanedmefagga",
]


CSRF_TRUSTED_ORIGINS = ['chrome-extension://eejfoncpjfgmeleakejdcanedmefagga']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_render_partial',

    'django.forms',

    'social_django',

    # our applications
    'spad_account',
    'spad_eshop_products',
    'spad_eshop_products_category',
    'spad_eshop_order',
    'spad_eshop_tag',
    'spad_eshop_slider',
    'spad_eshop_contact',
    'spad_eshop_settings',
    'spad_eshop_CustomersComments',
    'restFlutterAppStaff',
    'spad_buy_product',
    'captcha',

    'rest_framework',

    'rest_framework.authtoken',
    'sorl.thumbnail',

    'post_information',
    'mathfilters',
    # 'dj_rest_auth',
    # 'django.contrib.sites',

    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'dj_rest_auth.registration',

    # 'django_password_validators',
    # 'django_password_validators.password_history',
    # 'jalali_date',
    'django_jalali',
    # 'django_inlinecss',
    # 'phone_field'

]
FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'spadelc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'spadelc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Tehran'
#locale.setlocale(locale.LC_ALL, "fa_IR.UTF-8")
USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

STATIC_ROOT = os.path.join(BASE_DIR, "static_cdn", "static_root")
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "assets")
# ]



MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "static_cdn", "media_root")

# import spad_account
# from spad_account.models import User
# AUTH_USER_MODEL = User
AUTH_USER_MODEL = 'spad_account.User'
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jalali_date


# default settings
# JALALI_DATE_DEFAULTS = {
#    'Strftime': {
#         'date': '%y/%m/%d',
#         'datetime': '%H:%M:%S _ %y/%m/%d',
#     },
#     'Static': {
#         'js': [
#             # loading datepicker
#             'admin/js/django_jalali.min.js',
#             # OR
#             # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.core.js',
#             # 'admin/jquery.ui.datepicker.jalali/scripts/calendar.js',
#             # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc.js',
#             # 'admin/jquery.ui.datepicker.jalali/scripts/jquery.ui.datepicker-cc-fa.js',
#             # 'admin/js/main.js',
#         ],
#         'css': {
#             'all': [
#                 'admin/jquery.ui.datepicker.jalali/themes/base/jquery-ui.min.css',
#             ]
#         }
#     },
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django_password_validators.password_history.password_validation.UniquePasswordsValidator',
#         'OPTIONS': {
#              # How many recently entered passwords matter.
#              # Passwords out of range are deleted.
#              # Default: 0 - All passwords entered by the user. All password hashes are stored.
#             'last_passwords': 5 # Only the last 5 passwords entered by the user
#         }
#     },
# ]
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# hpotqpzjzonhlgfn
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_USE_TLS = True
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

#LOGIN_URL = '/auth/login/google-oauth2/'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'restFlutterAppStaff.permissions.IsStaffOrReadOnly',
        
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        #'rest_framework.authentication.BasicAuthentication',
        #'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        #jwt
        #knox
        #oauth
    ]
}

SITE_ID = 1
