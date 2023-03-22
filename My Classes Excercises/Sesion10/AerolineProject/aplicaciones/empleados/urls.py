from django.urls import path
from . import views

urlpatterns = [
    path('empleados/pagina-empleados', views.function_index),
    path('empleados/lista-empleados', views.listar_empleados),
]