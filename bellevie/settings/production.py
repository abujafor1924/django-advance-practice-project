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

# If we are in DEBUG mode or using ngrok, be more flexible
if DEBUG:
    ALLOWED_HOSTS.extend(['.ngrok-free.dev', '127.0.0.1', 'localhost', '*'])

import sys

# Check if we are running tests
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

# ===========================
# Security Settings
# ===========================
# Headers
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# SSL & HSTS
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=not (DEBUG or TESTING), cast=bool)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=31536000, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=True, cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=True, cast=bool)

# Cookies
# If SECURE_SSL_REDIRECT is False, we are likely on HTTP, so cookies shouldn't be 'Secure'
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=SECURE_SSL_REDIRECT, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=SECURE_SSL_REDIRECT, cast=bool)

# ===========================
# CORS & CSRF Trusted Origins
# ===========================
CORS_ALLOW_ALL_ORIGINS = config('CORS_ALLOW_ALL_ORIGINS', default=DEBUG, cast=bool)

if not CORS_ALLOW_ALL_ORIGINS:
    CORS_ALLOWED_ORIGINS_CONFIG = config('CORS_ALLOWED_ORIGINS', default='')
    if CORS_ALLOWED_ORIGINS_CONFIG:
        CORS_ALLOWED_ORIGINS = [s.strip() for s in CORS_ALLOWED_ORIGINS_CONFIG.split(',') if s.strip()]
    else:
        CORS_ALLOWED_ORIGINS = []

CSRF_TRUSTED_ORIGINS_CONFIG = config('CSRF_TRUSTED_ORIGINS', default='')
# We start with CSRF_TRUSTED_ORIGINS from base.py
if CSRF_TRUSTED_ORIGINS_CONFIG:
    additional_origins = [s.strip() for s in CSRF_TRUSTED_ORIGINS_CONFIG.split(',') if s.strip()]
    combined_origins = set(CSRF_TRUSTED_ORIGINS) | set(additional_origins)
else:
    combined_origins = set(CSRF_TRUSTED_ORIGINS)

# Automatically add https:// if http:// is present and vice versa for trusted domains
auto_origins = set()
for origin in combined_origins:
    if origin.startswith("http://"):
        auto_origins.add(origin.replace("http://", "https://"))
    elif origin.startswith("https://"):
        auto_origins.add(origin.replace("https://", "http://"))

CSRF_TRUSTED_ORIGINS = list(combined_origins | auto_origins)

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
