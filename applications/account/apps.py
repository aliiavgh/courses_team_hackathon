from django.apps import AppConfig
from django.core.signals import request_finished


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.account'

    def ready(self):
        from . import signals
        request_finished.connect(signals.create_profile, signals.save_profile)
