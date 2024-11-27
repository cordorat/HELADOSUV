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
    path('homeA/inventarioAdmin/helados/', views.mostrarHelados, name='helados'),
    path('homeA/inventarioAdmin/agregarHelado/', views.agregarHelado, name='agregarHelado'),   
    path('buscar_helado/<int:helado_id>/', views.buscarHelado, name='buscarHelado'),
    path('homeA/editarHelado/<int:helado_id>/', views.editar_helado, name='editarHelado'),

    path('homeA/gestionarEmpleado/crearEmpleado/', views.crearEmpleado, name='crearEmpleado'),
    path('homeA/gestionarEmpleado/empleados/', views.empleados, name='empleados'),
    path('buscar_empleado/', views.buscarEmpleado, name='buscar_empleado'),
    path('editar_empleado/<int:empleado_id>/', views.editarEmpleado, name='editar_empleado'),

    path('politicas/', views.politicas, name='politicas'),
    path('terminos/', views.terminos, name = 'terminos'),

    path('homeC/vendedoresCajero/crear_pedido/', views.crearPedido, name='crear_pedido'),
    path('homeC/vendedoresCajero/pedidos/', views.pedidos, name='pedidos'),
    path('editar_pedido/<int:pedido_id>/', views.editarPedido, name='editar_pedido'),
    path('buscar_pedido/', views.buscarPedido, name='buscar_pedido'),

    path('homeC/pedidosCajero/pedidosemp/', views.pedidosEmp, name='pedidosemp'),
    path('homeC/pedidosCajero/crear_pedido_emp/', views.crearPedidoEmpleado, name='crear_pedido_emp'),
    path('buscar_pedidos_menor/', views.buscarPedidoEmp, name='buscarpedidosemp'),
    path('editar_pedidos_menor/<int:pedido_id>', views.editarPedidoEmp, name='editarpedidosemp'),

    path('reporte/', views.reporte, name = 'reporte'),
]
