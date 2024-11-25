from django.db import models

# Create your models here.
class Helado (models.Model):
    marca = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    activo  = models.BooleanField(default=True)
    valor = models.IntegerField (blank= False)

    def __str__(self):
        return "Marca: " + self.marca + " - " + "Nombre: " +self.nombre 
    
class Empleado (models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    documento = models.IntegerField (blank= False)
    telefono = models.IntegerField(blank= False, default=0)
    activo = models.BooleanField(default=True)

