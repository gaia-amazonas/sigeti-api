from django.urls import path
from .views import traer_sexo_edad_territorial

urlpatterns = [
    path(
        "piramide_poblacional/<int:pk>/", traer_sexo_edad_territorial, name="get_actors"
    ),
]
