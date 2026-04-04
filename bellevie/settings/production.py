from decouple import config
import dj_database_url
from .base import *

SECURITY_KEY=config('SECRET_KEY')
DEBUG=config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS=config('ALLOWED_HOSTS', default='', cast=lambda v: [s.strip() for s in v.split(',')])


DATABASES = {
     "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("POSTGRES_DB"),
        "USER": config("POSTGRES_USER"),
        "PASSWORD": config("POSTGRES_PASSWORD"),
        "HOST": config("POSTGRES_HOST"),
        "PORT": config("POSTGRES_PORT"),
    },
    "backup": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": config("BACKUP_POSTGRES_DB"),
        "USER": config("BACKUP_POSTGRES_USER"),
        "PASSWORD": config("BACKUP_POSTGRES_PASSWORD"),
        "HOST": config("BACKUP_POSTGRES_HOST"),
        "PORT": config("BACKUP_POSTGRES_PORT"),
    },
}