from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    telefono= models.IntegerField()
    mensaje= models.CharField(max_length=180)

    def __str__(self):

       return f"NOMBRE: {self.nombre} MAIL: {self.mail} TELEFONO: {self.telefono}"

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    stock= models.IntegerField()
    precio= models.FloatField()
    categoria = models.CharField(max_length=20)
    URLimagen = models.CharField(max_length=160)
    descripcion = models.TextField()

    def __str__(self):

       return f"NOMBRE: {self.nombre} STOCK: {self.stock} PRECIO: {self.precio} CATEGORIA: {self.categoria} URLIMAGEN: {self.URLimagen} DESCRIPCION: {self.descripcion}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion = models.TextField()

    def __str__(self):

       return f"NOMBRE: {self.nombre} DESCRIPCION: {self.descripcion}"



class Avatar(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

  
    