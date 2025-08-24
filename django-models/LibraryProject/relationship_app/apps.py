<<<<<<< HEAD
# from django.apps import AppConfig


# class RelationshipAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'relationship_app'
# relationship_app/apps.py

from django.apps import AppConfig

class RelationshipAppConfig(AppConfig):
    name = 'relationship_app'

    def ready(self):
        import relationship_app.signals  # This imports the signals module
=======
from django.apps import AppConfig


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        import relationship_app.signals
>>>>>>> 8bb8dda1a481287b184dd5feb1ec3e7f69e36ec3
