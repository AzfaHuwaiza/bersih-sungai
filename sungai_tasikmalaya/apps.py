from django.apps import AppConfig

class SungaiTasikmalayaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sungai_tasikmalaya'

    def ready(self):
        import sungai_tasikmalaya.signals
