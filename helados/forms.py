from django.forms import ModelForm
from .models import Helado
from .models import Empleado
from .models import Pedido
from django import forms
from .models import Cliente
from .models import PedidoEmpleado

class agregarHeladoForm(ModelForm):
    class Meta:
        model = Helado
        fields = ['marca' , 'nombre', 'descripcion', 'activo' , 'valor']

class CrearEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'documento', 'telefono', 'activo']
        
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
        fields = ['codigo', 'producto', 'empleado']

    producto = forms.ModelMultipleChoiceField(
        queryset=Helado.objects.all(),  # Lista de productos disponibles
        widget=forms.CheckboxSelectMultiple,  # Puedes usar un widget para mostrar los productos como checkboxes
        required=True
    )

class BusquedaForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=False)

class BusquedaCodigoForm(forms.Form):
    query = forms.IntegerField(label='Buscar', required=False)

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nit', 'nombre', 'apellido', 'direccion' ]

class EmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['documento' ,'nombre', 'apellido', 'telefono']