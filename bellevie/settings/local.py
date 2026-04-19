from decouple import config
from .base import *
import dj_database_url

SECRET_KEY=config('SECRET_KEY')
DEBUG=config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS=config('ALLOWED_HOSTS', default='', cast=lambda v: [s.strip() for s in v.split(',') if s.strip()])

if DEBUG:
    ALLOWED_HOSTS += ['*', '192.168.0.245']


DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL', default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"))
}