from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Contacto, Producto, Avatar
from AppCoder.forms import ContactoFormulario, UserRegisterForm, UserEditForm, ProductosFormulario, AvatarFormulario
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required   

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def inicio(request):
    
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter( user = request.user.id)
        
      #   for a in avatar:
      #       cantidadDeAvatares = cantidadDeAvatares + 1
    
    
      #   diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url

    return render(request, 'AppCoder/inicio.html', diccionario)

def makeup(request):
   
   return render(request, "AppCoder/makeup.html")

def skincare(request):
   
   return render(request, "AppCoder/skincare.html")

def tienda(request):
   q = request.GET.get('busqueda', '')
   if q:
      productos = Producto.objects.filter(nombre__icontains=q)
      context = {"productos": productos,}
      
 
      return render(request, "AppCoder/tienda.html", context) 
   else:
      productos = Producto.objects.all()

      context = {"productos": productos,
              }
 
      return render(request, "AppCoder/tienda.html", context) 

   
def detalles(request, producto_id):
   obj = Producto.objects.get(pk=producto_id)
   context = {"producto": obj}

   return render(request, "AppCoder/detalles.html", context)

def nosotros(request):
   
   return render(request, "AppCoder/nosotros.html")  

def contacto(request):

   if request.method == "POST":

      miFormulario= ContactoFormulario(request.POST)
      if miFormulario.is_valid():
         informacion= miFormulario.cleaned_data

         contactoInsta = Contacto(nombre=informacion["nombre"], mail=informacion["mail"], telefono=informacion["telefono"], mensaje=informacion["mensaje"])
         contactoInsta.save()
         return render(request, "AppCoder/inicio.html")


   else:

      miFormulario= ContactoFormulario()   
   
   return render(request, "AppCoder/contacto.html", {"miFormulario": miFormulario})

def productosFormulario(request):

   if request.method == "POST":

      miFormulario= ProductosFormulario(request.POST)
      if miFormulario.is_valid():
         informacion= miFormulario.cleaned_data

         obj= Producto(

            nombre= informacion["nombre"],
            stock= informacion["stock"],
            precio= informacion["precio"],
            categoria = informacion["categoria"],
            URLimagen = informacion["URLimagen"],
            descripcion= informacion["descripcion"],
         )
         obj.save()

         productos = Producto.objects.all()

         context = {"productos": productos,
              }
         return render(request, "AppCoder/tienda.html", context)


   else:

      miFormulario= ProductosFormulario()   
   
   return render(request, "AppCoder/producto_form.html", {"miFormulario": miFormulario, "method": "POST"})

def editarProducto(request, producto_id):

   producto = Producto.objects.get(id= producto_id) 

   if request.method == "POST":

      miFormulario= ProductosFormulario(request.POST)
      if miFormulario.is_valid():
         informacion= miFormulario.cleaned_data

         producto.nombre= informacion["nombre"]
         producto.stock= informacion["stock"]
         producto.precio= informacion["precio"]
         producto.categoria = informacion["categoria"]
         producto.URLimagen = informacion["URLimagen"]
         producto.descripcion= informacion["descripcion"]
         

         

         producto.save()

         productos = Producto.objects.all()

         context = {"productos": productos,
              }
         return render(request, "AppCoder/tienda.html", context)


   else:

      miFormulario= ProductosFormulario(initial={
         "nombre":producto.nombre , 
         "stock":producto.stock , 
         "precio":producto.precio ,
         "categoria":producto.categoria ,
         "URLimagen": producto.URLimagen ,
         "descripcion":producto.descripcion ,

         })   

      context = {
         "miFormulario": miFormulario, 
         "producto": producto.nombre, 
         "method": "POST"}
   
   return render(request, "AppCoder/producto_form.html", context)


def eliminarProducto(request, producto_id):
   producto = Producto.objects.get(pk=producto_id) 
   producto.delete()

   productos=Producto.objects.all()

   return render(request, "AppCoder/tienda.html", {"productos":productos})

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from django.urls import reverse_lazy


from django.contrib.auth.forms import AuthenticationForm      
from django.contrib.auth import login, logout, authenticate

def login_request(request):

   if request.method=="POST":
      form = AuthenticationForm(request, data= request.POST)

      if form.is_valid():
         usuario= form.cleaned_data.get("username")
         contraseña= form.cleaned_data.get("password")

         user= authenticate(username=usuario, password=contraseña)

         if user is not None:

            login(request, user)
            return render(request, "AppCoder/inicio.html", {"mensaje": f"Bienvenido/a, {usuario}!!!!"})

         else:
            return render(request, "AppCoder/inicio.html", {"mensaje": f"Datos incorrectos!"})


      else:  

           return render(request, "AppCoder/inicio.html", {"mensaje": f"Formulario erróneo!!!!"})  


   form= AuthenticationForm() 

   return render(request, "AppCoder/login.html", {"form": form})  


def register(request):

   if request.method == "POST":
      form= UserRegisterForm(request.POST) 
      

      if form.is_valid():

         username= form.cleaned_data["username"]
         form.save()
         return render (request, "AppCoder/inicio.html", {"mensaje": f"{username} creado con éxito!!"})

   else:
      form= UserRegisterForm() 
       

   return render(request, "AppCoder/register.html", {"form": form})  



@login_required  
def editarPerfil(request):

   usuario= request.user

   if request.method == "POST":

      miFormulario= UserEditForm(request.POST)  

      if miFormulario.is_valid():

         informacion= miFormulario.cleaned_data

         usuario.email= informacion["email"] 
         usuario.password1= informacion["password1"]
         usuario.password2= informacion["password2"]
         usuario.last_name= informacion["last_name"]
         usuario.first_name= informacion["first_name"]

         usuario.save()

         return render(request, "AppCoder/inicio.html")

   else:
      miFormulario= UserEditForm(initial={"email":usuario.email})  

   return render (request, "AppCoder/editarPerfil.html", {"miFormulario":miFormulario, "usuario":usuario})       


@login_required
def agregarAvatar(request):
      if request.method == 'POST':

            miFormulario = AvatarFormulario(request.POST, request.FILES) 

            if miFormulario.is_valid():   


                  u = User.objects.get(username=request.user)
                
                  avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
      
                  avatar.save()

                  return render(request, "AppCoder/inicio.html") 

      else: 

            miFormulario= AvatarFormulario() 

      return render(request, "AppCoder/agregarAvatar.html", {"miFormulario":miFormulario})


