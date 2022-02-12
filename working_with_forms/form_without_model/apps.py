from django.apps import AppConfig


class FormWithoutModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'form_without_model'
