from django.db import models
from Aplicaciones.Categoria.models import Categoria

class Aplicacion(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField()
    version = models.CharField(max_length=100)
    fecha = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) 

    def __str__(self): 
        fila = "{0}:  {1}  {2}   {3} "
        return fila.format(self.id, self.nombre, self.descripcion, self.version, self.fecha)
