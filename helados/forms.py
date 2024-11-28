from django.forms import ModelForm
from .models import Helado
from .models import Empleado
from .models import Pedido
from django import forms
from .models import Cliente
from .models import PedidoEmpleado
from django.db.models import Sum, Avg, F, Count
from datetime import datetime

class agregarHeladoForm(ModelForm):
    class Meta:
        model = Helado
        fields = ['marca' , 'nombre', 'descripcion', 'activo' , 'valor']

class CrearEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'documento', 'telefono', 'activo']
    @staticmethod
    def contar_empleados():
        return Empleado.objects.count()

    @staticmethod
    def productividad_promedio(empleado_id=None):
        """
        Calcula la productividad promedio de todos los empleados.
        Si se pasa un empleado_id, calcula la productividad de ese empleado en particular.
        """
        if empleado_id:
            # Filtrar por un empleado específico
            empleado = Empleado.objects.get(id=empleado_id)
            total_pedidos = empleado.pedidos.count()
            total_horas = empleado.pedidos.aggregate(Sum('horas_trabajadas'))['horas_trabajadas__sum'] or 0
            if total_pedidos > 0:
                return total_horas / total_pedidos
            return 0
        else:
            # Para todos los empleados
            empleados = Empleado.objects.annotate(
                total_pedidos=Count('pedidos'),
                total_horas=Sum('pedidos__horas_trabajadas')
            ).aggregate(
                promedio_productividad=Avg(F('total_horas') / F('total_pedidos'))
            )
            return empleados['promedio_productividad'] or 0    
        
class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['codigo', 'producto']

    producto = forms.ModelMultipleChoiceField(
        queryset=Helado.objects.all(),  # Lista de productos disponibles
        widget=forms.CheckboxSelectMultiple,  # Puedes usar un widget para mostrar los productos como checkboxes
        required=True
    )

class PedidoEmpleadoForm(ModelForm):
    class Meta:
        model = PedidoEmpleado
        fields = ['codigo', 'producto', 'empleado', 'fecha', 'horaTrabajada']

    producto = forms.ModelMultipleChoiceField(
        queryset=Helado.objects.all(),  # Lista de productos disponibles
        widget=forms.CheckboxSelectMultiple,  # Puedes usar un widget para mostrar los productos como checkboxes
        required=True
    )
    

class BusquedaForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=True)

class BusquedaCodigoForm(forms.Form):
    query = forms.IntegerField(label='Buscar', required=False)

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nit', 'nombre', 'apellido', 'direccion' ]

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['documento' ,'nombre', 'apellido', 'telefono',]

class ReporteForm(forms.Form):
    # Filtro para horas trabajadas (dia, mes, año)
    filtro_horas = forms.ChoiceField(choices=[('dia', 'Día'), ('mes', 'Mes'), ('anio', 'Año')], required=False)
    
    