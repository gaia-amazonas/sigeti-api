from django.urls import path
from .views import traer_sexo_edad_territorial, traer_infraeastructura_comunal
from .views_total import traer_porcentaje_total

urlpatterns = [
    path(
        "piramide_poblacional/territorio/<int:pk>/",
        traer_sexo_edad_territorial,
        name="traer_sexo_edad_territorial",
    ),
    path(
        "infraestructura/comunidad/<int:pk>/",
        traer_infraeastructura_comunal,
        name="traer_infraeastructura_comunal",
    ),
    path(
        "lengua/total/",
        lambda request: traer_porcentaje_total(request, variable="LenguasCnida"),
        name="traer_porcentaje_total_lengua",
    ),
]
