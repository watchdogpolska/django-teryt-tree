DEBUG = True
USE_TZ = True
SECRET_KEY = "pQO26MjmglIoVGG40wrOmYOHYKr2R6EFOhxZHaFwlz6LpLvQ49"
DATABASES = {
    "default": {"ENGINE": "django.db.backends.sqlite3", "NAME": "database.sqlite3"}
}
ROOT_URLCONF = "tests.urls"
INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "teryt_tree",
    "tests",
]
SITE_ID = 1
MIDDLEWARE_CLASSES = ()
