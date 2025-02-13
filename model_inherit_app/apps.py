from django.apps import AppConfig


class ModelInheritAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'model_inherit_app'
