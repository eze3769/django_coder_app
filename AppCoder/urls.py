from django.urls import path
from AppCoder import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path('makeup', views.makeup, name= "Makeup"),
    path('skincare', views.skincare, name= "Skincare"),
    path('tienda', views.tienda, name= "Tienda"),
    path('contacto', views.contacto, name= "Contacto"),
    path('nosotros', views.nosotros, name= "Nosotros"),
    path('detalles/<int:producto_id>/', views.detalles, name= "Detalles"),
    path('productos/nuevo/', views.productosFormulario, name= "Nuevo"),
    path('productos/<int:producto_id>/borrar', views.eliminarProducto, name= "Borrar"),
    path('productos/<int:producto_id>/', views.editarProducto, name= "Editar"),
    path('login', views.login_request, name= "Login"),
    path('register', views.register, name= "Register"),
    path('logout', LogoutView.as_view(template_name= "AppCoder/logout.html"), name= "Logout"),
    path('editarPerfil', views.editarPerfil, name= "EditarPerfil"),
    path('agregarAvatar', views.agregarAvatar, name="AgregarAvatar"),
    
]