from django.shortcuts import render, redirect
from .models import Aplicacion
from django.contrib import messages
from django.conf import settings
import os

def inicio(request):
    lisyadoAplicacion = Aplicacion.objects.all()
    return render(request, "inicio.html", {'Aplicacion': lisyadoAplicacion})

# Renderizar el formulario para nueva prueba
def nuevoCajero(request):
    return render(request, "nuevoCajero.html")

# Función encargada de guardar una nueva prueba en la base de datos
def guardarCajero(request):
    nombre = request.POST["nombre"]
    cedula = request.POST["cedula"]
    turno = request.POST["turno"]

    #Subiendo archivo con parentecis
    logo=request.FILES.get("logo")
    pdf=request.FILES.get("pdf")

    Cajeros.objects.create(nombre=nombre, cedula=cedula, turno=turno, logo=logo, pdf=pdf)

    #Mensaje de confirmacion 
    messages.success(request, "Cajero guardado exitosamente")
    return redirect('inicio')

# Eliminar una prueba por ID
def eliminarCajero(request, id):
    cajeroElimiar = Cajeros.objects.get(id=id)

    if cajeroElimiar.logo and os.path.isfile(os.path.join(settings.MEDIA_ROOT, cajeroElimiar.logo.name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, cajeroElimiar.logo.name))

    if cajeroElimiar.pdf and os.path.isfile(os.path.join(settings.MEDIA_ROOT, cajeroElimiar.pdf.name)):
        os.remove(os.path.join(settings.MEDIA_ROOT, cajeroElimiar.pdf.name))

    cajeroElimiar.delete()
    return redirect('inicio')

# Mostrando formulario de ediccion
def editarCajero(request, id):
    cajeroEditar = Cajeros.objects.get(id=id)
    return render(request, "editarCajero.html", {'cajeroEditar': cajeroEditar})

def procesarEdicionCajeros(request):
    
    id=request.POST["id"]
    nombre = request.POST["nombre"]
    cedula = request.POST["cedula"]
    turno = request.POST["turno"]
    logo=request.FILES.get("logo")
    pdf=request.FILES.get("pdf")
    
    cajeros2=Cajeros.objects.get(id=id)
    cajeros2.nombre=nombre
    cajeros2.cedula=cedula
    cajeros2.turno=turno
    if logo :
        if cajeros2.logo:
            rutaLogo = os.path.join(settings.MEDIA_ROOT, str(cajeros2.logo))
            if os.path.isfile(rutaLogo):
                os.remove(rutaLogo)
        cajeros2.logo = logo

    if pdf:
        if cajeros2.pdf:
            rutaPdf = os.path.join(settings.MEDIA_ROOT, str(cajeros2.pdf))
            if os.path.isfile(rutaPdf):
                os.remove(rutaPdf)
        cajeros2.pdf = pdf
        
    cajeros2.save()
    #Mensaje de confirmacion
    messages.success(request, "Cajero Actualizado exitosamente")
    return redirect('inicio')

