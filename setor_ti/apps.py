from django.apps import AppConfig


class SetorTiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'setor_ti'

    def ready(self):
        import setor_ti.signals