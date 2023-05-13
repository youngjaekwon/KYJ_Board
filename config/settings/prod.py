import os

import environ

from .base import *

env = environ.Env(DEBUG=(bool, False))
environ.Env.read_env(env_file=os.path.join(BASE_DIR, ".env"))

DEBUG = False
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += []

REST_FRAMEWORK.update(
    {"DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",)}
)

CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"

DATABASES = {
    "default": {
        "ENFINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": "postgres",
        "PORT": 5432,
    }
}
