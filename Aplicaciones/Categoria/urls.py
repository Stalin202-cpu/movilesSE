from django.urls import path
from . import views

urlpatterns = [
    path('inicio2',views.inicio2,name='inicio2'),  # este name debe coincidir con tu plantilla
    path('nuevaCategoria', views.nuevaCategoria),
    path('guardarCategoria', views.guardarCategoria),
    path('eliminarCategoria/<id>', views.eliminarCategoria),
    path('editarCategoria/<id>', views.editarCategoria),
    path('procesarEdicionCategoria', views.procesarEdicionCategoria, name='procesarEdicionCategoria'),
    ]