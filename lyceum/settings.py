from distutils.util import strtobool
from pathlib import Path

from dotenv import dotenv_values, find_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

env_vars = dotenv_values(find_dotenv())

BASE_DIR = Path(__file__).resolve().parent.parent

env_vars = dotenv_values(find_dotenv())

SECRET_KEY: str = env_vars["SECRET_KEY"]

DEBUG: bool = strtobool(env_vars["DEBUG"])

ALLOWED_HOSTS: list = [] if DEBUG else env_vars["ALLOWED_HOSTS"].split(" ")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "about",
    "catalog",
    "homepage"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "lyceum.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "lyceum.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation\
              .UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation\
              .MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.\
              CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.\
              NumericPasswordValidator"}
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
