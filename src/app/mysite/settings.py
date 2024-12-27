import environ
 
env = environ.Env()
env.read_env('.env')
 
SECRET_KEY = env('SECRET_KEY')
# SECURITY WARNING: keep the secret key used in production secret!
#   SECRET_KEY


import os
from pathlib import Path

from datetime import timedelta #JWT



# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False
TEMPLATE_DEBUG = DEBUG


#ALLOWED_HOSTS = ['localhost', '192.168.0.229']
# ALLOWED_HOSTS = []
ALLOWED_HOSTS=["160.251.77.161", "localhost", "factioproject.com"]



# Build paths inside the project like this: BASE_DIR / 'subdir'.
# TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


BASE_DIR = Path(__file__).resolve().parent.parent

#STATIC_DIR = os.path.join(BASE_DIR, 'static')

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# 静的ファイル配置先のディレクトリへのURL。http://ドメイン名:ポート名/static/フォルダ/ファイル名でアクセスできるようになる
#STATIC_URL = '/static/'

STATIC_URL = 'static/'
MEDIA_URL = '/media/'


if DEBUG:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
else:
    STATIC_ROOT = '/usr/share/nginx/html/static'
    MEDIA_ROOT = '/usr/share/nginx/html/media'



#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

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
    # 'accounts_jwt',
    # 'rest_framework' #JWT認証

    # 'xadmin'
    # 'crispy_forms',
    # 'xadmin',

    # 'social_django',  # ソーシャルログイン
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'social_django.middleware.SocialAuthExceptionMiddleware',  # ソーシャルログイン
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

                # 'social_django.context_processors.backends',  # ソーシャルログイン
                # 'social_django.context_processors.login_redirect', # ソーシャルログイン
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'factio',
        'USER': 'HEW',
        'PASSWORD': '@HEW2023',
        'HOST': 'localhost',
    }
}
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'django_boards',
#         'USER': 'muramoto',
#         'PASSWORD' : '',
#         'HOST' : 'localhost',
#         'PORT' : 5432,
#     }
# }

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
EMAIL_HOST_USER = 'factiohew@gmail.com'
EMAIL_HOST_PASSWORD = 'gzqbctsqnujtaars'
EMAIL_USE_TLS = True



#自動ログアウト
# デフォルトは二週間後
#セッション時間
# SESSION_COOKIE_AGE = 60 * 60 #60 * 5 = 5分
#最後にアクセスしてからの測定
SESSION_SAVE_EVERY_REQUEST = True


# REST_FRAMEWORK = {
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.IsAuthenticated',
#     ],
#     'DEFAULT_AUTHENTICATION_CLASSES':[
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ]
# }

# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
#     'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
#     'ROTATE_REFRESH_TOKENS': False,
#     'BLACKLIST_AFTER_ROTATION': False,
#     'AUTH_HEADER_TYPES': ('Bearer', ),
#     'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', )
# }


# AUTH_USER_MODEL = 'accounts_jwt.UserAccount' #JWT


# ソーシャルログイン
# AUTHENTICATION_BACKENDS = (
#     'social_core.backends.open_id.OpenIdAuth',
#     'social_core.backends.google.GoogleOpenId',
#     'social_core.backends.google.GoogleOAuth2',

#     'social_core.backends.github.GithubOAuth2',
#     'social_core.backends.twitter.TwitterOAuth',
#     'social_core.backends.facebook.FacebookOAuth2',

#     'django.contrib.auth.backends.ModelBackend',
# )

# ソーシャルログイン
# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'home'

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '892295542692-5ia4t2endls2560lelii5mp199n13dec.apps.googleusercontent.com'  # クライアントID
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '892295542692-5ia4t2endls2560lelii5mp199n13dec.apps.googleusercontent.com' # クライアント シークレット
