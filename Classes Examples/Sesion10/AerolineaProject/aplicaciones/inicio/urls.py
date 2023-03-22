from django.urls import path
from . import views

urlpatterns = [
    path('inicio/pagina-inicial/', views.funcion_index),
    path('inicio/lista-personas/', views.listar_personas),
]