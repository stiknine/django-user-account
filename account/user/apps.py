from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    verbose_name = gettext_lazy('User Account')

    def ready(self):
        from . import signals
