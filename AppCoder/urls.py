from django.urls import path
from AppCoder import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('inicio', views.inicio, name= "Inicio"),
    path('makeup', views.makeup, name= "Makeup"),
    path('skincare', views.skincare, name= "Skincare"),
    path('contacto', views.contacto, name= "Contacto"),
    path('nosotros', views.nosotros, name= "Nosotros"),
    path('busquedaCremas', views.busquedaCremas, name= "BusquedaCremas"),
    path('buscarCremas/', views.buscarCremas),
    path('leerLabiales', views.leerLabiales, name= "LeerLabiales"),
    path('eliminarLabial/<nombre_para_borrar>/', views.eliminarLabial, name= "EliminarLabial"),
    path('editarLabial/<nombre_para_editar>/', views.editarLabial, name= "EditarLabial"),
    path('labialesFormulario', views.labialesFormulario, name= "LabialesFormulario"),
    path('cremas/list', views.CremasList.as_view(), name= "List"),
    path(r'^(?P<pk>\d+)$', views.CremasDetalle.as_view(), name= "Detail"),
    path(r'^nuevo$', views.CremasCreacion.as_view(), name= "New"),
    path(r'^editar/(?P<pk>\d+)$', views.CremasUpdate.as_view(), name= "Edit"), 
    path(r'^borrar/(?P<pk>\d+)$', views.CremasDelete.as_view(), name= "Delete"), 
    path('login', views.login_request, name= "Login"),
    path('register', views.register, name= "Register"),
    path('logout', LogoutView.as_view(template_name= "AppCoder/logout.html"), name= "Logout"),
    path('editarPerfil', views.editarPerfil, name= "EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    
]