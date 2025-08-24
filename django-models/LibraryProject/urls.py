from django.urls import path, include

urlpatterns = [
    path("", include("django_models.urls")),  # include your app urls
]
