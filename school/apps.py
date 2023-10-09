from django.apps import AppConfig


class SchoolConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "school"

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        # noinspection PyUnresolvedReferences
        from . import signals
