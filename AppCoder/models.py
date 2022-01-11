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



class Labiales(models.Model):
    nombre = models.CharField(max_length=40)
    stock= models.IntegerField()
    precio= models.IntegerField()

    def __str__(self):

       return f"LABIAL: {self.nombre} STOCK: {self.stock} PRECIO: {self.precio}"


class Cremas(models.Model):
    nombre = models.CharField(max_length=40)
    stock= models.IntegerField()
    precio= models.IntegerField()

    def __str__(self):

       return f"CREMA: {self.nombre} STOCK: {self.stock} PRECIO: {self.precio}"  


class Avatar(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

  
    