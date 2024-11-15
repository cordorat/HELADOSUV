from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import django.db
from .forms import agregarHeladoForm
from .models import Helado

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

def mostrarHelados (request):
    helados = Helado.objects.filter()
    return render (request, 'helados.html', {
        'helados' : helados
    })

def politicas (request):
    return render(request,'politicas.html')
