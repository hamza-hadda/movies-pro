from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CoreConfig(AppConfig):
    name = "movie_core.core"
    verbose_name = _("Core")

    def ready(self):
        from django.core.management import call_command
        call_command('load_fixtures')

