from decouple import config
import dj_database_url
from .base import *

SECRET_KEY = config('SECRET_KEY', default='django-insecure-fallback-key-for-prod-test')
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS_CONFIG = config('ALLOWED_HOSTS', default='localhost,127.0.0.1')
ALLOWED_HOSTS = [s.strip() for s in ALLOWED_HOSTS_CONFIG.split(',') if s.strip()]


DATABASES = {
     "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
    },
}