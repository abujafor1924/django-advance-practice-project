from decouple import config
from .base import *
import dj_database_url

SECRET_KEY=config('SECRET_KEY')
DEBUG=config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS=config('ALLOWED_HOSTS', default='', cast=lambda v: [s.strip() for s in v.split(',')])


DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}