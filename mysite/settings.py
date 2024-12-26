import environ

env = environ.Env()
env.read_env('.env')

SECRET_KEY = env('SECRET_KEY')

import os
from pathlib import Path

from datetime import timedelta #JWT

#DEBUG = True
DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_URL = 'static/'
MEDIA_URL = '/media/'


if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    STATIC_ROOT = '/usr/share/nginx/html/static'
    MEDIA_ROOT = '/usr/share/nginx/html/media'

# 静的ファイルの配置先。この例では、STATIC_DIR(BASE_DIR/static)が設定される。
STATICFILES_DIRS = [
    #(STATIC_DIR),
    ('account', STATIC_ROOT + '/accounts/'),
    ('media', MEDIA_ROOT),
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'app',
    'accounts',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django.contrib.humanize', #カンマ

    'bootstrap_datepicker_plus', #カレンダー 誕生日
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_I10N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'none'

# --------------------------------------------
AUTH_USER_MODEL = 'accounts.CustomUser'
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False

NUMBER_GROUPING = 3 #カンマ区切り

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'XXX@gmail.com' # 任意のメールアドレス
EMAIL_HOST_PASSWORD = '' # 発行されたパスワード
EMAIL_USE_TLS = True

#自動ログアウト
# デフォルトは二週間後
#セッション時間
# SESSION_COOKIE_AGE = 60 * 60 #60 * 5 = 5分
#最後にアクセスしてからの測定
SESSION_SAVE_EVERY_REQUEST = True