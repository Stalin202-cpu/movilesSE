from django.shortcuts import render, redirect
from .models import Categoria
from django.contrib import messages

# Vista para mostrar el listado de categorías
def inicio2(request):
    listadoCategorias = Categoria.objects.all()
    return render(request, "inicio2.html", {'categorias': listadoCategorias})

# Vista para mostrar el formulario de nueva categoría
def nuevaCategoria(request):
    return render(request, "nuevaCategoria.html")

# Vista para guardar una nueva categoría
def guardarCategoria(request): 
    nombre = request.POST["nombre"]

    Categoria.objects.create(nombre=nombre)

    messages.success(request, "Categoría creada exitosamente")
    return redirect('inicio2')

# Vista para eliminar una categoría
def eliminarCategoria(request, id):

    categoriaEliminar = Categoria.objects.get(id=id)

    categoriaEliminar.delete()

    messages.success(request, "Categoría eliminada exitosamente")
    return redirect('inicio2')

# Vista para mostrar el formulario de edición
def editarCategoria(request, id):
    categoriaEditar = Categoria.objects.get(id=id)
    return render(request, "editarCategoria.html", {'categoriaEditar': categoriaEditar})

# Vista para procesar la edición
def procesarEdicionCategoria(request):
    id_categoria = request.POST["id"]
    categoria2 = Categoria.objects.get(id=id_categoria)
    categoria2.nombre = request.POST["nombre"]

    categoria2.save()

    messages.success(request, "Categoría actualizada exitosamente")
    return redirect('inicio2')
