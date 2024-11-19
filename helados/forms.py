from django.forms import ModelForm
from .models import Helado
from .models import Empleado


class agregarHeladoForm(ModelForm):
    class Meta:
        model = Helado
        fields = ['marca' , 'nombre', 'descripcion', 'activo' , 'valor']

class CrearEmpleadoForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'documento', 'telefono', 'activo']
