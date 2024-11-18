from django.db import models

# Create your models here.
class Helado (models.Model):
    marca = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    valor = models.IntegerField (blank= False)

    def __str__(self):
        return "Marca: " + self.marca + " - " + "Nombre: " +self.nombre 
