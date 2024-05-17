from django.urls import path
from .views import traer_actores

urlpatterns = [
    path("actores/", traer_actores, name="get_actors"),
]
