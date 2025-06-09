# C:\proyectos-django\laboratorioSJ\Aplicaciones\pruebaLaboratorio\urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('inicio',views.inicio,name='inicio'),
    path('nuevaAplicacion', views.nuevaAplicacion),  # corregido
    path('guardarAplicacion', views.guardarAplicacion),  # corregido
    path('eliminarAplicacion/<id>', views.eliminarAplicacion),  # corregido
    path('editarAplicacion/<id>',views.editarAplicacion),
    path('procesarEdicionAplicacion', views.procesarEdicionAplicacion)
]
