from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def _str_(self):
        fila = "{0}: {1}"
        return fila.format(self.id, self.nombre)