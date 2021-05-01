from django.apps import AppConfig


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello'

    def ready(self):
        print("starting scheduler ...")
        from .Scheduler import updater
        updater.start()
