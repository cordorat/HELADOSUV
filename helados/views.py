from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import django.db 
from .forms import agregarHeladoForm, CrearEmpleadoForm, PedidoForm, BusquedaForm, ClienteForm, PedidoEmpleadoForm, BusquedaCodigoForm, CambiarContraseniaForm
from .models import Helado
from .models import Empleado
from .models import Pedido, PedidoEmpleado
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomPasswordChangeForm
from django.contrib.auth import update_session_auth_hash




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
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'inicio_cajero.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o contrasena es incorrecto'
            })
        else:
            login(request, user)
            return redirect('homeC')


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
            return redirect('helados')
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
            return render(request, 'editar_helado.html', {'helado': helado, 'form': form, 'error': "Error, no se pudo actualizar."})


def politicas(request):
    return render(request, 'politicas.html')


def terminos(request):
    return render(request, 'terminos.html')


def crearEmpleado(request):
    if request.method == 'GET':
        return render(request, 'crear_empleado.html', {'form': CrearEmpleadoForm})
    else:
        try:
            form = CrearEmpleadoForm(request.POST)
            nuevo_empleado = form.save(commit=False)
            nuevo_empleado.save()
            return redirect('empleados')
        except ValueError:
            return render(request, 'crear_empleado.html', {'form': CrearEmpleadoForm, 'error': 'No se ha podido crear el perfil del Empleado'})


def empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados})


def buscarEmpleado(request):
    form = BusquedaForm(request.GET)
    print(form)
    # Si el formulario se ha enviado con un término de búsqueda
    empleados = Empleado.objects.all()  # Obtiene todos los empleados por defecto

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            # Filtra los empleados por nombre (insensible a mayúsculas/minúsculas)
            empleados = empleados.filter(nombre__icontains=query)

    return render(request, 'buscar_empleado.html', {'form': form, 'empleados': empleados})


def editarEmpleado(request, empleado_id):
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
            return render(request, 'editar_empleados.html', {'empleado': empleado, 'form': form, 'error': "No se pudo editar el perfil de empleado."})


def crearPedido(request):
    if request.method == 'GET':
        return render(request, 'crear_pedido.html', {
            'form': PedidoForm, 'form1': ClienteForm
        })
    else:
        try:
            
            form = PedidoForm(request.POST)
            form1 = ClienteForm(request.POST)
            nuevo_cliente = form1.save()

            nuevo_pedido = form.save(commit=False)
            nuevo_pedido.cliente = nuevo_cliente
            
            nuevo_pedido.save()

            return redirect('pedidos')
        except ValueError:
            return render(request, 'crear_pedido.html', {
                'form': PedidoForm, 'form1': ClienteForm,
                'error': 'No se ha podido crear el Pedido o el Cliente'
            })


def crearPedidoEmpleado(request):
    if request.method == 'GET':
        return render(request, 'crear_pedido_emp.html', {
            'form': PedidoEmpleadoForm
        })
    else:
        try:
            form = PedidoEmpleadoForm(request.POST)
            nuevo_pedido = form.save(commit=False)

            nuevo_pedido.save()

            return redirect('pedidosemp')
        except ValueError:
            return render(request, 'crear_pedido_emp.html', {
                'form': PedidoEmpleadoForm,
                'error': 'No se ha podido crear el Pedido'
            })


def pedidosEmp(request):
    form = BusquedaCodigoForm(request.POST)
    # Obtiene todos los empleados por defecto
    pedidos = PedidoEmpleado.objects.all()
    buscar_realizado = False
    error_busqueda = None

    if request.method == 'POST':
        buscar_realizado = True
        if form.is_valid():
                query = form.cleaned_data['query']
                if query:
                    try:
                        query = int(query)
                        pedidos = pedidos.filter(codigo=query)
                        if not pedidos:
                            error_busqueda = "No existe el pedido"
                    except ValueError:
                        error_busqueda = "El codigo debe ser valido"
                else:
                    error_busqueda = "El campo no puede estar vacio"
                    
    
    return render(request, 'pedidos_emp.html', {'form': form, 
                                                'pedidos': pedidos, 
                                                'buscar_realizado': buscar_realizado, 
                                                'error_busqueda' : error_busqueda})
def cancelarPedidoEmp (request, pedido_codigo):
    pedido = get_object_or_404 (Pedido, pk = pedido_codigo)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidosemp')


def buscarPedidoEmp(request):
    form = BusquedaCodigoForm(request.POST)
    # Obtiene todos los empleados por defecto
    pedidos = PedidoEmpleado.objects.all()
    buscar_realizado = False
    error_busqueda = None

    if request.POST:
        buscar_realizado = True
    try:
        if form.is_valid():
            query = form.cleaned_data['query']
            if not query:
                raise ValueError("El campo no puede estar vacio")
            
            query = int(query)
            pedidos = pedidos.filter(codigo=query)
        
    
    except ValueError as e:
            error_busqueda = str(e)
            
    return render(request, 'buscar_pedido_emp.html', {'form': form, 'pedidos': pedidos, 'buscar_realizado': buscar_realizado, 'error_busqueda' : error_busqueda})
            


def editarPedidoEmp(request, pedido_codigo):
    if request.method == 'GET':
        pedido = get_object_or_404(PedidoEmpleado, pk=pedido_codigo)
        form = PedidoEmpleadoForm(instance=pedido)
        return render(request, 'editar_pedido_emp.html', {'pedido': pedido, 'form': form})
    else:
        try:
            pedido = get_object_or_404(PedidoEmpleado, pk=pedido_codigo)
            form = PedidoEmpleadoForm(request.POST, instance=pedido)
            form.save()
            return redirect('pedidosemp')
        except ValueError:
            return render(request, 'editar_pedido_emp.html', {'pedido': pedido, 'form': form, 'error': "No se pudo editar el pedido."})


def empleadoAdmin(request):
    return render(request, 'empleado_admin.html')


def pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedidos.html', {'pedidos': pedidos})

def cancelarPedido (request, pedido_codigo):
    pedido = get_object_or_404 (Pedido, pk = pedido_codigo)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos')


def editarPedido(request, pedido_codigo):
    if request.method == 'GET':
        pedido = get_object_or_404(Pedido, pk=pedido_codigo)
        form = PedidoForm(instance=pedido)
        return render(request, 'editar_pedido.html', {'pedido': pedido, 'form': form})
    else:
        try:
            pedido = get_object_or_404(Pedido, pk=pedido_codigo)
            form = PedidoForm(request.POST, instance=pedido)
            form.save()
            return redirect('pedidos')
        except ValueError:
            return render(request, 'editar_pedido.html', {'pedido': pedido, 'form': form, 'error': "No se pudo editar el pedido."})


def buscarPedido(request):
    form = BusquedaCodigoForm(request.GET)
    print(form)
    # Si el formulario se ha enviado con un término de búsqueda
    pedidos = Pedido.objects.all()  # Obtiene todos los empleados por defecto

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            query = int(query)
            pedidos = pedidos.filter(codigo=query)
    return render(request, 'buscar_pedido.html', {'form': form, 'pedidos': pedidos})


def reportesAdmin(request):
    return render(request, 'reportes_admin.html')


def inventarioAdmin(request):
    return render(request, 'inventario_admin.html')


def vendedoresCajero(request):
    return render(request, 'vendedores_cajero.html')


def pedidosCajero(request):
    return render(request, 'pedidos_cajero.html')


def cajaCajero(request):
    return render(request, 'caja_cajero.html')

def ayuda(request):
    return render(request,'ayuda.html')

def olvidar(request):
    form = BusquedaForm(request.POST)
    form2 = CambiarContraseniaForm(request.POST)

    print("Formulario Busqueda:", form)  # Verificar el formulario de búsqueda
    print("Formulario Cambio Contraseña:", form2)  # Verificar el formulario de contraseña

    usuario = None  # Inicializamos la variable usuario

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            # Filtra los usuarios por correo electrónico
            
            usuario = User.objects.filter(email__icontains=query).first()  # Obtiene el primer usuario que coincida
            print("Usuario encontrado:", usuario)  # Verificamos que el usuario sea correcto

            if usuario:
                if request.method == 'POST':  # Solo procesamos si el método es POST
                    print("Procesando formulario de cambio de contraseña")
                    if form2.is_valid():
                        # Si el formulario de contraseña es válido
                        print("Formulario de cambio de contraseña es válido")
                        nueva_contrasenia = form2.cleaned_data['nueva_contrasenia']

                        # Cambiar la contraseña
                        usuario.set_password(nueva_contrasenia)
                        usuario.save()  # Guarda los cambios

                        # Mantener la sesión activa después de cambiar la contraseña
                        messages.success(request, "¡Tu contraseña ha sido cambiada exitosamente!")
                        return redirect('home')  # Redirige a la página de inicio o donde prefieras
                    else:
                        print("Errores en el formulario de cambio de contraseña:", form2.errors)
                        messages.error(request, "Por favor, corrige los errores en el formulario.")
                else:
                    # Si no es POST, muestra el formulario vacío
                    form2 = CambiarContraseniaForm()

                return render(request, 'olvidar.html', {'form': form, 'form2': form2})
            else:
                # Si no se encuentra el usuario
                messages.error(request, "No se encontró un usuario con ese correo.")
                return render(request, 'olvidar.html', {'form': form, 'form2': form2})
        else:
            # Si no se ingresa un correo en el formulario de búsqueda
            messages.error(request, "Por favor, ingresa un término de búsqueda.")
            return render(request, 'olvidar.html', {'form': form, 'form2': form2})

    return render(request, 'olvidar.html', {'form': form, 'form2': form2})



@login_required
def editarPerfil(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()  # Guarda la nueva contraseña
            update_session_auth_hash(request, user)  # Mantiene al usuario logueado
            messages.success(request, '¡Tu contraseña se cambió con éxito!')
            return redirect('home')  # Redirige a la página deseada
        else:
            messages.error(request, 'Corrige los errores en el formulario.')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'editar_perfil.html', {'form': form})

def reporte_inventario(request): 
    helados = Helado.objects.all() 
    return render(request, 'reporte_inventario.html', {'helados': helados})