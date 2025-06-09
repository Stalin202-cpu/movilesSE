from django.shortcuts import render, redirect
from .models import Aplicacion
from django.contrib import messages
from django.conf import settings
import os

def inicio(request):
    lisyadoAplicacion = Aplicacion.objects.all()
    return render(request, "inicio.html", {'Aplicacion': lisyadoAplicacion})

# Renderizar el formulario para nueva prueba
def nuevaAplicacion(request):
    return render(request, "nuevaAplicacion.html")

# Función encargada de guardar una nueva prueba en la base de datos
def guardarAplicacion(request):
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    version = request.POST["version"]
    fecha = request.POST["fecha"]

    #Subiendo archivo con parentecis

    Aplicacion.objects.create(nombre=nombre, descripcion=descripcion, version=version, fecha=fecha)

    #Mensaje de confirmacion 
    messages.success(request, "Aplicacion guardado exitosamente")
    return redirect('inicio')

# Eliminar una prueba por ID
def eliminarAplicacion(request, id):
    aplicacionEliminar = Aplicacion.objects.get(id=id)
    aplicacionEliminar.delete()
    return redirect('inicio')

# Mostrando formulario de ediccion
def editarAplicacion(request, id):
    cajeroAplicacion = Aplicacion.objects.get(id=id)
    return render(request, "editarAplicacion.html", {'cajeroAplicacion': cajeroAplicacion})

def procesarEdicionCajeros(request):
    
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    descripcion = request.POST["descripcion"]
    version = request.POST["version"]
    fecha = request.POST["fecha"]
    
    aplicacion2=Aplicacion.objects.get(id=id)
    aplicacion2.nombre=nombre
    aplicacion2.descripcion=descripcion
    aplicacion2.version=version
    aplicacion2.fecha=fecha
        
    aplicacion2.save()
    #Mensaje de confirmacion
    messages.success(request, "Aplicacion Actualizado exitosamente")
    return redirect('inicio')

