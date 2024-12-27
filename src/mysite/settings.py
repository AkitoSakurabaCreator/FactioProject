import environ

env = environ.Env()
env.read_env('.env')

SECRET_KEY = env('SECRET_KEY')

import os
from pathlib import Path

from datetime import timedelta

DEBUG = True
# DEBUG = False # 本番ではTrueにしてください。
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost'] # 任意のIP

BASE_DIR = Path(__file__).resolve().parent.parent

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 静的ファイル配置先のディレクトリへのURL。http://ドメイン名:ポート名/static/フォルダ/ファイル名でアクセスできるようになる

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

    'allauth.account.middleware.AccountMiddleware', #Django 5から
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


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_I10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'none'

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# --------------------------------------------
AUTH_USER_MODEL = 'accounts.CustomUser' #元
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False



NUMBER_GROUPING = 3 #カンマ区切り

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# メールをコンソールに表示する
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True



#自動ログアウト
# デフォルトは二週間後
#セッション時間
#最後にアクセスしてからの測定
SESSION_SAVE_EVERY_REQUEST = True