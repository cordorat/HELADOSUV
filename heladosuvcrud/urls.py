"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from helados import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),

    path('singup/', views.singUp, name='singup'),
    path('logout/', views.cerrarSesion, name='logout'),
    path('singinA/', views.iniciarSesionAdmin, name='singinA'),
    path('singinC/', views.iniciarSesionCajero, name='singinC'),

    path('homeA/', views.homeAdmin, name='homeA'),
    path('homeC/', views.homeCajero, name='homeC'),

    #A partir de admin
    path('homeA/gestionarEmpleado/',views.empleadoAdmin, name='gestionarEmpleado'),
    path('homeA/reportesAdmin/', views.reportesAdmin, name='reportesAdmin'),
    path('homeA/inventarioAdmin/', views.inventarioAdmin, name='inventarioAdmin'),

    #A partir de cajero
    path('homeC/vendedoresCajero/', views.vendedoresCajero, name='vendedoresCajero'),
    path('homeC/pedidosCajero/', views.pedidosCajero, name='pedidosCajero'),
    path('homeC/cajaCajero/', views.cajaCajero, name='cajaCajero'),

    #CRUD Helado
    path('helados/', views.mostrarHelados, name='helados'),
    path('agregar_helado/', views.agregarHelado, name='agregarHelado'),   
    path('buscar_helado/<int:helado_id>/', views.buscarHelado, name='buscarHelado'),
    path('editar_helado/<int:helado_id>/', views.editar_helado, name='editarHelado'),

    path('homeA/gestionarEmpleado/crearEmpleado/', views.CrearEmpleado, name='crearEmpleado'),
    path('empleados/', views.Empleados, name='empleados'),
    path('buscar_empleado/', views.BuscarEmpleado, name='buscar_empleado'),
    path('homeA/gestionarEmpleado/editar_empleado/<int:empleado_id>/', views.EditarEmpleado, name='editar_empleado'),

    path('politicas/', views.politicas, name='politicas'),
    path('terminos/', views.terminos, name = 'terminos'),

    path('crear_pedido/', views.CrearPedido, name='crear_pedido'),
    path('pedidos/', views.Pedidos, name='pedidos'),
    path('editar_pedido/<int:pedido_id>/', views.EditarPedido, name='editar_pedido'),
    path('buscar_pedido/', views.BuscarPedido, name='buscar_pedido'),
    path('crear_pedido_emp/', views.CrearPedidoEmpleado, name='crear_pedido_emp'),
]
