"""
Django settings for backend project.
Production-ready for Render deployment
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD

=======
>>>>>>> c2cabf8e7ed723401e921398187f1df065cf6cb1
# SECURITY


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "unsafe-dev-secret")

DEBUG = os.getenv("DJANGO_DEBUG", "False") == "True"

ALLOWED_HOSTS = [
    "law-firm-backend-rqjz.onrender.com",
    "eredilawadvocates.web.app",
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = [
    "https://eredilawadvocates.web.app",
]


# APPLICATIONS


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party
    "corsheaders",
    "rest_framework",

    # Local apps
    "api",
]


# DJANGO REST FRAMEWORK


REST_FRAMEWORK = {
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",       
        "rest_framework.parsers.MultiPartParser",  
    ],
}

# MIDDLEWARE


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

<<<<<<< HEAD

=======
>>>>>>> c2cabf8e7ed723401e921398187f1df065cf6cb1
# CORS


CORS_ALLOW_ALL_ORIGINS = False

CORS_ALLOWED_ORIGINS = [
    "https://eredilawadvocates.web.app",
]

CORS_ALLOW_CREDENTIALS = True


# URLS / WSGI


ROOT_URLCONF = "backend.urls"
WSGI_APPLICATION = "backend.wsgi.application"

<<<<<<< HEAD
=======

>>>>>>> c2cabf8e7ed723401e921398187f1df065cf6cb1
# TEMPLATES


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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


# DATABASE 


if os.environ.get("DATABASE_URL"):
    DATABASES = {
        "default": dj_database_url.config(
            conn_max_age=600,
            ssl_require=True,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# PASSWORD VALIDATION


AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# INTERNATIONALIZATION


LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# STATIC FILES


STATIC_URL = "/static/"


STATIC_ROOT = BASE_DIR / "staticfiles"


STATICFILES_DIRS = [
    BASE_DIR / "static",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# MEDIA FILES


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

<<<<<<< HEAD
# CSRF / SESSION (Firebase-safe)
=======

# CSRF / SESSION 
>>>>>>> c2cabf8e7ed723401e921398187f1df065cf6cb1


CSRF_COOKIE_SAMESITE = "None"
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = "None"
SESSION_COOKIE_SECURE = True





# EMAIL CONFIGURATION


EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND",
    "django.core.mail.backends.smtp.EmailBackend",
)

EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL",
    EMAIL_HOST_USER,
)


# LOGGING 


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
