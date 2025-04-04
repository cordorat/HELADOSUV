from django.forms import ModelForm
from .models import Helado
from .models import Empleado
from .models import Pedido
from django import forms
from .models import Cliente
from .models import PedidoEmpleado
from django.contrib.auth.forms import PasswordChangeForm


class agregarHeladoForm(ModelForm):
    class Meta:
        model = Helado
        fields = ['marca' , 'nombre', 'descripcion', 'activo' , 'valor', 'stock']

class CrearEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'documento', 'telefono', 'activo']
      
        
class PedidoForm(ModelForm):
    class Meta:
        model = Pedido
        fields = ['producto']

    producto = forms.ModelMultipleChoiceField(
    queryset=Helado.objects.all(),  # Lista de productos disponibles
    widget=forms.CheckboxSelectMultiple,  # Puedes usar un widget para mostrar los productos como checkboxes
    required=True
    )

class PedidoEmpleadoForm(ModelForm):
    class Meta:
        model = PedidoEmpleado
        fields = ['producto', 'empleado']

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


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].label = "Contraseña actual"
        self.fields['new_password1'].label = "Nueva contraseña"
        self.fields['new_password2'].label = "Confirmar nueva contraseña"
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': field.label,
            })   

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico", max_length=254)    

class CambiarContraseniaForm(forms.Form):
    nueva_contrasenia = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Nueva Contraseña'}),
        min_length=8,
        label="Nueva Contraseña"
    )
    confirmar_contrasenia = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Contraseña'}),
        min_length=8,
        label="Confirmar Contraseña"
    )

    def clean(self):
        cleaned_data = super().clean()
        nueva_contrasenia = cleaned_data.get("nueva_contrasenia")
        confirmar_contrasenia = cleaned_data.get("confirmar_contrasenia")

        if nueva_contrasenia and confirmar_contrasenia:
            if nueva_contrasenia != confirmar_contrasenia:
                raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data