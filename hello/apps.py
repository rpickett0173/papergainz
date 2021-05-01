from django.apps import AppConfig
import datetime


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hello'

    def ready(self):
        print("starting scheduler ...")
        print(datetime.datetime.today())
        from .Scheduler import updater
        updater.start()
