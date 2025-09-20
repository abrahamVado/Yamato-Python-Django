import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'dev-secret')
DEBUG = os.getenv('DJANGO_DEBUG', 'True').lower() == 'true'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.sessions.middleware.SessionMiddleware' if False else 'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'yamato_auth_django.urls'

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

WSGI_APPLICATION = 'yamato_auth_django.wsgi.application'

# DB: default to SQLite for quick start; override with DATABASE_URL env for Postgres
if os.getenv('DATABASE_URL'):
    import dj_database_url  # type: ignore
    DATABASES = {'default': dj_database_url.parse(os.environ['DATABASE_URL'], conn_max_age=600)}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Password hashing: use Argon2id
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Static
STATIC_URL = 'static/'

# DRF basics (no default auth for now; endpoints are stubs)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}

# CORS for cross-site cookies
CORS_ALLOW_CREDENTIALS = True
_raw_origins = os.getenv('CORS_ORIGINS', 'http://localhost:3000')
CORS_ALLOWED_ORIGINS = [o.strip() for o in _raw_origins.split(',') if o.strip()]

# Security headers (also set in views/middleware as needed)
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Cookies (your app will set yamato_rt/at explicitly; Django session cookie not used)
COOKIE_DOMAIN = os.getenv('COOKIE_DOMAIN', '.yamato.local')
COOKIE_SECURE = os.getenv('COOKIE_SECURE', 'True').lower() == 'true'
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = COOKIE_SECURE
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = COOKIE_SECURE
