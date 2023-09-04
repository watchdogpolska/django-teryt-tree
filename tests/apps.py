from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TestConfig(AppConfig):
    name = "tests"
    default_auto_field = 'django.db.models.AutoField'