from decouple import config
import dj_database_url
from .base import *

# ===========================
# Basic Settings
# ===========================
SECRET_KEY = config('SECRET_KEY', default='django-insecure-fallback-key-for-prod-test')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS_CONFIG = config('ALLOWED_HOSTS', default='localhost,127.0.0.1')
ALLOWED_HOSTS = [s.strip() for s in ALLOWED_HOSTS_CONFIG.split(',') if s.strip()]

# ===========================
# Security Settings
# ===========================
# Headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# Cookies
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=True, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=True, cast=bool)

# SSL & HSTS
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=True, cast=bool)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=31536000, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True, cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=True, cast=bool)

# ===========================
# CORS & CSRF Trusted Origins
# ===========================
CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS_CONFIG = config('CORS_ALLOWED_ORIGINS', default='')
CORS_ALLOWED_ORIGINS = [s.strip() for s in CORS_ALLOWED_ORIGINS_CONFIG.split(',') if s.strip()]

CSRF_TRUSTED_ORIGINS_CONFIG = config('CSRF_TRUSTED_ORIGINS', default='')
CSRF_TRUSTED_ORIGINS = [s.strip() for s in CSRF_TRUSTED_ORIGINS_CONFIG.split(',') if s.strip()]

# ===========================
# Database Configuration
# ===========================
# Use DATABASE_URL if provided, otherwise build from POSTGRES_* variables
DATABASE_URL = config('DATABASE_URL', default=None)

if DATABASE_URL:
    DATABASES = {
        'default': dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            conn_health_checks=True,
        )
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('POSTGRES_DB'),
            'USER': config('POSTGRES_USER'),
            'PASSWORD': config('POSTGRES_PASSWORD'),
            'HOST': config('POSTGRES_HOST'),
            'PORT': config('POSTGRES_PORT'),
        }
    }
