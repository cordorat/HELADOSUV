from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import django.db
from .forms import agregarHeladoForm
from .models import Helado
from .forms import CrearEmpleadoForm
from .models import Empleado

# Create your views here.


def home(request):
    return render(request, 'home.html')


def singUp(request):
    if request.method == 'GET':
        return render(request, 'singup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except django.db.IntegrityError:
                return render(request, 'singup.html', {
                    'form': UserCreationForm,
                    'error': 'El nombre de usuario ya existe'
                })
        return render(request, 'singup.html', {
            'form': UserCreationForm,
            'error': 'Las contrasenas no coinciden'
        })


def cerrarSesion(request):
    logout(request)
    return redirect('home')


def iniciarSesionAdmin(request):
    if request.method == 'GET':
        return render(request, 'inicio_admin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'inicio_admin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contrasena es incorrecto'
            })
        else:
            login(request, user)
            return redirect('homeA')


def iniciarSesionCajero(request):
    if request.method == 'GET':
        return render(request, 'inicio_cajero.html', {
            'form': AuthenticationForm
        })


def homeAdmin(request):
    return render(request, 'home_admin.html')


def homeCajero(request):
    return render(request, 'home_cajero.html')


def agregarHelado(request):
    if request.method == 'GET':
        return render(request, 'agregar_helado.html', {
            'form': agregarHeladoForm
        })
    else:
        try:
            form = agregarHeladoForm(request.POST)
            nuevo_helado = form.save(commit=False)
            nuevo_helado.save()
            return redirect('homeA')
        except ValueError:
            return render(request, 'agregar_helado.html', {
                'form': agregarHeladoForm,
                'error': 'No se ha podido agregar el helado'
            })


def mostrarHelados(request):
    helados = Helado.objects.filter()
    return render(request, 'lista_helados.html', {
        'helados': helados
    })


def buscarHelado(request, helado_id):
    helado = get_object_or_404(Helado, pk=helado_id)
    return render(request, 'buscar_helado.html', {
        'helado': helado
    })


def editar_helado(request, helado_id):

    if request.method == 'GET':
        helado = get_object_or_404(Helado, pk=helado_id)
        form = agregarHeladoForm(instance=helado)
        return render(request, 'editar_helado.html', {'helado': helado, 'form': form})
    else:
        try:
            helado = get_object_or_404(Helado, pk=helado_id)
            form = agregarHeladoForm(request.POST, instance=helado)
            form.save()
            return redirect('helados')
        except ValueError:
            return render(request, 'editar_helado.html', {'helado': helado, 'form': form, 'error' : "Error, no se pudo actualizar."})


def politicas(request):
    return render(request, 'politicas.html')


def terminos(request):
    return render(request, 'terminos.html')


def CrearEmpleado(request):
    if request.method == 'GET':
        return render(request, 'crear_empleado.html', {'form': CrearEmpleadoForm})
    else:
        try:
            form=CrearEmpleadoForm(request.POST)
            nuevo_empleado =form.save(commit=False)
            nuevo_empleado.save()
            return redirect('empleados')
        except ValueError:
            return render(request, 'crear_empleado.html', {'form': CrearEmpleadoForm, 'error': 'No se ha podido crear el perfil del Empleado'})



def Empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})

def BuscarEmpleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    return render(request, 'buscar_empleado.html', {'empleado': empleado})

def EditarEmpleado(request, empleado_id):
    if request.method == 'GET':
        empleado = get_object_or_404(Empleado, pk=empleado_id)
        form = CrearEmpleadoForm(instance=empleado)
        return render(request, 'editar_empleado.html', {'empleado': empleado, 'form': form})
    else:
        try:
            empleado = get_object_or_404(Empleado, pk=empleado_id)
            form = CrearEmpleadoForm(request.POST, instance=empleado)
            form.save()
            return redirect('empleados')
        except ValueError:
            return render(request, 'editar_empleados.html', {'empleado': empleado, 'form': form, 'error' : "No se pudo editar el perfil de empleado."})