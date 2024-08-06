"""
Django settings for apps project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import datetime
import logging
import os
import socket
import sys

import environ

CONFIG_DIR = environ.Path(__file__) - 1
BASE_DIR = environ.Path(__file__) - 3


env = environ.Env(
    DJANGO_ENVIRONMENT=(str, "production"),  # development, production, test
    DJANGO_DEBUG=(bool, False),
    DJANGO_ADMIN_URL=(str, "admin/"),
    DJANGO_SECRET_KEY=(str, ""),
    DJANGO_ALLOWED_HOSTS=(list, ["127.0.0.1", "localhost"]),
    DJANGO_SESSION_COOKIE_SECURE=(bool, True),
    DJANGO_SECURE_HSTS_SECONDS=(int, 0),
    DJANGO_CACHE_URL=(str, "locmemcache://"),
    DJANGO_DATABASE_URL=(str, "sqlite:///sqlite.db"),
    DJANGO_DEFAULT_FROM_EMAIL=(str, "TEST: tickie <noreply@tickie.io>"),
    DJANGO_EMAIL_BACKEND=(str, "django.core.mail.backends.console.EmailBackend"),
    DJANGO_EMAIL_URL=(environ.Env.email_url_config, "consolemail://"),
    DJANGO_BACKEND_URL=(str, "http://localhost:8000"),
    DJANGO_FRONTEND_URL=(str, "http://localhost:3000"),
    # Files
    DJANGO_STATIC_ROOT=(str, str(BASE_DIR("staticfiles"))),
    # Auth
    DJANGO_AXES_BEHIND_REVERSE_PROXY=(bool, False),
    # Debug
    DJANGO_SENTRY_DSN=(str, ""),
    DJANGO_SENTRY_ENVIRONMENT=(str, "local"),
    DJANGO_SENTRY_RELEASE=(str, "<sha>"),
    DJANGO_SENTRY_TRACES_SAMPLE_RATE=(float, 0.1),
    DJANGO_SENTRY_LOG_LEVEL=(int, logging.INFO),
    DJANGO_DEBUG_TOOLBAR_USE_DOCKER=(bool, True),
)

# OS environment variables take precedence over variables from those files:
env.read_env(str(CONFIG_DIR(".env")))
env.read_env(str(CONFIG_DIR("development.env")))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env("DJANGO_DEBUG")
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "Europe/Berlin"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-GB"
# https://docs.djangoproject.com/en/dev/ref/settings/#languages
# from django.utils.translation import gettext_lazy as _
# LANGUAGES = [
#     ('en', _('Englisch')),
#     ('de', _('Deutsch')),
#     ('fr-fr', _('Französisch')),
# ]
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(BASE_DIR("locale"))]

# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {"default": env.db("DJANGO_DATABASE_URL")}

# https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-DEFAULT_AUTO_FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "apps.config.urls"
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
# WSGI_APPLICATION = "config.wsgi.application"
WSGI_APPLICATION = "apps.config.wsgi.application"

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",  # Handy template tags
    "django.forms",
]
THIRD_PARTY_APPS = [
    "axes",
    "ambient_toolbox",
    "django_components",
    # https://pypi.org/project/django-components/
    # This is a drop-in replacement for django.contrib.staticfiles.
    # Its behavior is 100% identical except it ignores .py and .html files,
    # meaning these will not end up on your static files server.
    # To use it, add it to INSTALLED_APPS and remove django.contrib.staticfiles.
    "django_components.safer_staticfiles",
    "django_htmx",
    "health_check",  # required
    "health_check.db",  # stock Django health checkers
    "health_check.cache",
    "health_check.contrib.migrations",
]

LOCAL_APPS = [
    "apps.account",
    "apps.check_in",
    "apps.core",
    "apps.event",
    "apps.guest",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    "axes.backends.AxesBackend",
    "django.contrib.auth.backends.ModelBackend",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "account.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "account:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "account_login"

# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "kolo.middleware.KoloMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "ambient_toolbox.middleware.current_user.CurrentUserMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    # AxesMiddleware should be the last middleware in the MIDDLEWARE list.
    "axes.middleware.AxesMiddleware",
]


# STORAGES
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = env("DJANGO_STATIC_ROOT")
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [str(CONFIG_DIR("../static"))]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(BASE_DIR("media"))

# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"


# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # https://docs.djangoproject.com/en/dev/ref/settings/#dirs
        "DIRS": [str(BASE_DIR("templates"))],
        # https://docs.djangoproject.com/en/dev/ref/settings/#app-dirs
        "APP_DIRS": True,
        "OPTIONS": {
            # https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# https://docs.djangoproject.com/en/dev/ref/settings/#form-renderer
FORM_RENDERER = "django.forms.renderers.TemplatesSetting"

# FIXTURES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#fixture-dirs
FIXTURE_DIRS = (str(BASE_DIR("fixtures")),)

# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
vars().update(env.email_url("DJANGO_EMAIL_URL"))
EMAIL_BACKEND = env("DJANGO_EMAIL_BACKEND")
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5

DEFAULT_FROM_EMAIL = env("DJANGO_DEFAULT_FROM_EMAIL")

# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL.
ADMIN_URL = env("DJANGO_ADMIN_URL")
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = [("""christoph-teichmeister""", "christoph.teichmeister@gmail.com")]
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
# https://cookiecutter-django.readthedocs.io/en/latest/settings.html#other-environment-settings


# testing part

TEST_RUNNER = "apps.utils.runners.PytestTestRunner"

if "pytest" in sys.modules:
    # TODO: think about dedicated file so it's compatible to unittest runner
    # loads specific environment for unittests
    environ.Env.read_env(env_file=CONFIG_DIR("unittest.env"))

    # following settings will speed up the test runner:

    # Use a fast, insecure password hasher
    PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]

    # Use in-memory cache and mail backend
    EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    STORAGES["default"] = {
        "BACKEND": "inmemorystorage.InMemoryStorage",
    }

    # We want templates to show useful errors even when DEBUG is set to False:
    TEMPLATES[0]["OPTIONS"]["debug"] = True

    MEDIA_URL = "http://media.testserver"

    # Enable whitenoise autscanning
    WHITENOISE_AUTOREFRESH = True

# Exclude main app from database serialization, speeds up tests, but removes ability to simulate rollbacks in tests
TEST_NON_SERIALIZED_APPS = ["apps"]

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY")
ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS")

# adds the container's internal IP to the allowed hosts to enable healthchecks w/o Host-header:
ALLOWED_HOSTS.append(socket.gethostbyname(socket.gethostname()))

# CACHES
# ------------------------------------------------------------------------------
CACHES = {
    "default": env.cache("DJANGO_CACHE_URL"),
}

if env("DJANGO_ENVIRONMENT") == "development":
    # WhiteNoise
    # ------------------------------------------------------------------------------
    # http://whitenoise.evans.io/en/latest/django.html#using-whitenoise-in-development
    INSTALLED_APPS = ["whitenoise.runserver_nostatic", *INSTALLED_APPS]

    # django-debug-toolbar
    # ------------------------------------------------------------------------------
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
    INSTALLED_APPS += ["debug_toolbar"]
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
    # https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
    DEBUG_TOOLBAR_CONFIG = {
        "DISABLE_PANELS": [
            "debug_toolbar.panels.redirects.RedirectsPanel",
            "debug_toolbar.panels.profiling.ProfilingPanel",
        ],
        "SHOW_TEMPLATE_CONTEXT": True,
    }
    # https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
    INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
    if env("DJANGO_DEBUG_TOOLBAR_USE_DOCKER"):
        hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
        INTERNAL_IPS += [".".join(ip.split(".")[:-1] + ["1"]) for ip in ips]

    # django-extensions
    # ------------------------------------------------------------------------------
    # https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
    INSTALLED_APPS += ["django_extensions"]

# SECURITY
# ------------------------------------------------------------------------------
# Use X-Forwarded-Proto Header to determine SSL status (useful for API docs)
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = False  # HTTP to HTTPS redirection will be done at load balancer level.
CSRF_COOKIE_SECURE = SESSION_COOKIE_SECURE = env("DJANGO_SESSION_COOKIE_SECURE")
SECURE_BROWSER_XSS_FILTER = SECURE_CONTENT_TYPE_NOSNIFF = True

SILENCED_SYSTEM_CHECKS = [
    # SECURE_SSL_REDIRECT can be False because redirection at application level is not needed.
    # We serve via AWS load balancers which do that already:
    "security.W008",
]

SECURE_HSTS_SECONDS = env("DJANGO_SECURE_HSTS_SECONDS")
if SECURE_HSTS_SECONDS > 0:
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True

# Set URLs and URL-Protocol for CORS and CSRF settings
FRONTEND_URL = env("DJANGO_FRONTEND_URL")
BACKEND_URL = env("DJANGO_BACKEND_URL")
URL_PROTOCOL = "https://" if SESSION_COOKIE_SECURE else "http://"

# LOGGING
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#logging
# See https://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
DJANGO_LOG_LEVEL = "INFO" if DEBUG else "ERROR"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        }
    },
    "root": {"level": "INFO", "handlers": ["console"]},
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": DJANGO_LOG_LEVEL,
            "propagate": True,
        },
        "django.db.backends": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
        # Errors logged by the SDK itself
        "sentry_sdk": {"level": "ERROR", "handlers": ["console"], "propagate": False},
        "django.security.DisallowedHost": {
            "level": "ERROR",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

# Sentry
if os.environ.get("DJANGO_SENTRY_DSN"):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration
    from sentry_sdk.integrations.logging import LoggingIntegration

    sentry_logging = LoggingIntegration(
        level=env("DJANGO_SENTRY_LOG_LEVEL"),  # Capture info and above as breadcrumbs
        event_level=logging.ERROR,  # Send errors as events
    )

    sentry_sdk.init(
        dsn=env("DJANGO_SENTRY_DSN"),
        integrations=[sentry_logging, DjangoIntegration()],
        max_breadcrumbs=50,
        debug=False,
        environment=env("DJANGO_SENTRY_ENVIRONMENT"),
        release=env("DJANGO_SENTRY_RELEASE"),
        server_name=BACKEND_URL,
        send_default_pii=True,
        traces_sample_rate=env("DJANGO_SENTRY_TRACES_SAMPLE_RATE"),
    )

# Set the session cookie age to 48 hours (172800 seconds)
SESSION_COOKIE_AGE = 60 * 60 * 48
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

# Referrer-Policy middleware
REFERRER_POLICY = "same-origin"

# Cross-Origin Resource Sharing
CORS_ALLOW_CREDENTIALS = True
CORS_URLS_REGEX = "/api/.*"

CORS_ALLOWED_ORIGINS = (FRONTEND_URL,)

CSRF_TRUSTED_ORIGINS = [
    FRONTEND_URL,
    BACKEND_URL,
]


# Axes config
LOGIN_TIMEDELTA = 15 * 60
LOGIN_COUNT = 3
AXES_COOLOFF_TIME = datetime.timedelta(0, LOGIN_TIMEDELTA)
AXES_LOGIN_FAILURE_LIMIT = LOGIN_COUNT
AXES_USERNAME_FORM_FIELD = "username"
AXES_CLEANUP_DAYS = 30
# Block by Username only (i.e.: Same user different IP is still blocked, but different user same IP is not)
AXES_LOCKOUT_PARAMETERS = ["username"]
# Disable logging the IP-Address of failed login attempts by returning None for attempts to get the IP
# Ignore assigning a lambda function to a variable for brevity
AXES_CLIENT_IP_CALLABLE = lambda x: None  # noqa: E731
# Mask user-sensitive parameters in logging stream
AXES_SENSITIVE_PARAMETERS = ["username", "email", "ip_address"]
