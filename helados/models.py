from django.db import models

# Create your models here.
class Helado (models.Model):
    marca = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    activo  = models.BooleanField(default=True)
    valor = models.IntegerField (blank= False)
    stock = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return "Marca: " + self.marca + " - " + "Nombre: " +self.nombre 
    
class Empleado (models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    documento = models.IntegerField (blank= False)
    telefono = models.IntegerField(blank= False, default=0)
    activo = models.BooleanField(default=True)
    

    def __str__(self):
        return "Nombre: " + self.nombre + " - " + "Apellido: " + self.apellido

class Cliente (models.Model):
    nit = models.IntegerField(blank=False)
    nombre= models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)

    def __str__(self):
        return "Nombre: " + self.nombre + " - " + "Apellido: " +self.apellido


class Pedido (models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ManyToManyField(Helado, related_name='pedidoshela')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')

class PedidoEmpleado (models.Model):
    codigo = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    producto = models.ManyToManyField(Helado, related_name='pedidosemp')
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='pedidosemp') 

class RegistroHoras(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name="registros")
    horas_trabajadas = models.DecimalField(max_digits=5, decimal_places=2)
    fecha = models.DateField()
    