from django.forms import ModelForm
from .models import Helado


class agregarHeladoForm(ModelForm):
    class Meta:
        model = Helado
        fields = ['marca' , 'nombre', 'descripcion', 'valor']