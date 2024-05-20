from django.urls import path
from .views import traer_nombres

urlpatterns = [
    path(
        "nombres/",
        traer_nombres,
        name="traer_nombres_de_territorio",
    ),
]
