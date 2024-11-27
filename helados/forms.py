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
        fields = ['nombre', 'apellido', 'documento', 'telefono', 'activo', 'horaTrabajada']
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
        fields = ['codigo', 'producto', 'empleado', 'fecha']

    producto = forms.ModelMultipleChoiceField(
        queryset=Helado.objects.all(),  # Lista de productos disponibles
        widget=forms.CheckboxSelectMultiple,  # Puedes usar un widget para mostrar los productos como checkboxes
        required=True
    )
    def horas_trabajadas_totales(filtro=None):
        """
        Devuelve las horas trabajadas de todos los empleados, con la posibilidad
        de filtrar por un día, mes o año específico.
        """
        if filtro:
            hoy = datetime.now()

            if filtro == "dia":
                return Pedido.objects.filter(fecha=hoy.date()).aggregate(Sum('horas_trabajadas'))['horas_trabajadas__sum'] or 0
            elif filtro == "mes":
                return Pedido.objects.filter(fecha__month=hoy.month, fecha__year=hoy.year).aggregate(Sum('horas_trabajadas'))['horas_trabajadas__sum'] or 0
            elif filtro == "anio":
                return Pedido.objects.filter(fecha__year=hoy.year).aggregate(Sum('horas_trabajadas'))['horas_trabajadas__sum'] or 0
        else:
            # Si no se pasa filtro, se suman todas las horas trabajadas
            return Pedido.objects.aggregate(Sum('horas_trabajadas'))['horas_trabajadas__sum'] or 0

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
    
    # Filtro para empleado (si el usuario desea filtrar por empleado para la productividad promedio)
    empleado_id = forms.IntegerField(required=False, label="ID del empleado")