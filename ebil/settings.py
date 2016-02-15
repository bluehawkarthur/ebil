"""
Django settings for ebil project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9fzbh^dl_t)t3f_hu=hbi@5t%92$=$zh1rsov_e=xxr2r01%4i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# ====== configure for django-excel =======
FILE_UPLOAD_HANDLERS = ("django_excel.ExcelMemoryFileUploadHandler",
                        "django_excel.TemporaryExcelFileUploadHandler")

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # use for local ad not produccion 
    # 'debug_toolbar',
    # aplicaciones
    'apps.users',
    'apps.inicio',
    'apps.proveedores',
    'apps.producto',
    # 'apps.almacenes',
    'apps.cliente',
    'apps.compras',
    'apps.reportes',
    'apps.ventas',
    'apps.config',
    #librerias
    # 'captcha',
    'nocaptcha_recaptcha',
    'widget_tweaks',
    'django_extensions',
    'rolepermissions',
    'imagekit',
    'qrcode',
)

MIDDLEWARE_CLASSES = (
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'ebil.urls'

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
                'django.template.context_processors.media',
                'apps.inicio.process_role.rol',
            ],
        },
    },
]

WSGI_APPLICATION = 'ebil.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# ------------------base de datos local --------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ebil1',
        'USER': 'root',
        'PASSWORD': '1',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }
}

# ========== Database for produccion ==============================
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'd47512b9tqcqjl',
#         'USER':'uwybtnhtgnbyqu',
#         'PASSWORD': 'edge96Ow3pKLeOng926Rch7XCO',
#         'HOST': 'ec2-54-197-241-24.compute-1.amazonaws.com',
#         'PORT': '5432',
        
#     }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
AUTH_USER_MODEL = 'users.User'

LANGUAGE_CODE = 'es-bo'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

RECAPTCHA_PUBLIC_KEY = '6LcVu9ESAAAAANVWwbM5-PLuLES94GQ2bIYmSNTG'
RECAPTCHA_PRIVATE_KEY = '6LcVu9ESAAAAAGxz7aEIACWRa3CVnXN3mFd-cajP'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# ======== configure for user roles ===========
ROLEPERMISSIONS_MODULE = 'apps.inicio.roles'


STATIC_ROOT = 'staticfiles'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ======= configure for django recaptcha =========

NORECAPTCHA_SITE_KEY  = '6LfeIg0TAAAAAKNqc6kXnxJoNkmtZByMJC-X2wfV'
NORECAPTCHA_SECRET_KEY  = '6LfeIg0TAAAAAD1rb1X8vu8BbPJ2DZ4JIJP9tlGF'

if DEBUG:

    from fnmatch import fnmatch
    class glob_list(list):
        def __contains__(self, key):
            for elt in self:
                if fnmatch(key, elt): return True
            return False

    INTERNAL_IPS = glob_list(['127.0.0.1', '192.168.*.*'])

# ======= configure for debug toolbar =====

# DEBUG_TOOLBAR_PATCH_SETTINGS = True
# INTERNAL_IPS = ('127.0.0.1',)

