from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Contacto, Cremas, Labiales, Avatar
from AppCoder.forms import ContactoFormulario, LabialesFormulario, UserRegisterForm, UserEditForm, AvatarFormulario
from django.contrib.auth.models import User

# Create your views here.
def inicio(request):
    
    diccionario = {}
    cantidadDeAvatares = 0
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter( user = request.user.id)
        
        for a in avatar:
            cantidadDeAvatares = cantidadDeAvatares + 1
    
    
        diccionario["avatar"] = avatar[cantidadDeAvatares-1].imagen.url

    #return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'AppCoder/inicio.html', diccionario)

def makeup(request):
   
   return render(request, "AppCoder/makeup.html")

def skincare(request):
   
   return render(request, "AppCoder/skincare.html")

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

def busquedaCremas(request):
   return render(request, "AppCoder/busquedaCremas.html")


def buscarCremas(request):

   if request.GET["nombre"]:
      nombre= request.GET["nombre"]

      cremas= Cremas.objects.filter(nombre__icontains=nombre)
    #  respuesta= f"Estoy buscando a: {request.GET['nombre']}"
      return render(request, "AppCoder/resultadoBusqueda.html", {"cremas": cremas, "nombre": nombre})

   else:
      respuesta= "Ingresá una crema"

   return HttpResponse(respuesta)

from django.contrib.auth.decorators import login_required   

@login_required
def leerLabiales(request):
   labiales= Labiales.objects.all()
   dir={"labiales":labiales} #contexto
   return render(request, "AppCoder/leerLabiales.html", dir)


def eliminarLabial(request, nombre_para_borrar):
   labialQueQuieroBorrar = Labiales.objects.get(nombre=nombre_para_borrar)  
   labialQueQuieroBorrar.delete()

   labiales=Labiales.objects.all()

   return render(request, "AppCoder/leerLabiales.html", {"labiales":labiales})


def editarLabial(request, nombre_para_editar):

   labiales = Labiales.objects.get(nombre=nombre_para_editar) 

   if request.method == "POST":

      miFormulario= LabialesFormulario(request.POST)
      if miFormulario.is_valid():
         informacion= miFormulario.cleaned_data

      

         labiales.nombre= informacion["nombre"]
         labiales.stock= informacion["stock"]
         labiales.precio= informacion["precio"]

         

         labiales.save()

         return render(request, "AppCoder/inicio.html")


   else:

      miFormulario= LabialesFormulario(initial={"nombre":labiales.nombre, "stock":labiales.stock, "precio":labiales.precio})   
   
   return render(request, "AppCoder/editarLabial.html", {"miFormulario": miFormulario, "nombre_para_editar": nombre_para_editar})



def labialesFormulario(request):

   if request.method == "POST":

      miFormulario= LabialesFormulario(request.POST)
      if miFormulario.is_valid():
         informacion= miFormulario.cleaned_data

         lab= Labiales(

            nombre= informacion["nombre"],
            stock= informacion["stock"],
            precio= informacion["precio"]

         )
         lab.save()
         return render(request, "AppCoder/makeup.html")


   else:

      miFormulario= LabialesFormulario()   
   
   return render(request, "AppCoder/labialesFormulario.html", {"miFormulario": miFormulario})



from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#from django.urls import reverse_lazy

class CremasList(ListView):
   model = Cremas
   template_name= "AppCoder/cremas_list.html"

class CremasDetalle(DetailView):   
   model= Cremas
   template_name= "AppCoder/cremas_detalle.html"


class CremasCreacion(CreateView):

    model = Cremas
    success_url = "../AppCoder/cremas/list"
    fields = ['nombre', 'stock', 'precio'] 


class CremasUpdate(UpdateView):

      model = Cremas
      success_url = "../cremas/list"
      fields  = ['nombre', 'stock', 'precio'] 


class CremasDelete(DeleteView):

      model = Cremas
      success_url = "../cremas/list"


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


