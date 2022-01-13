from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Contacto)

admin.site.register(Producto)

admin.site.register(Categoria)

admin.site.register(Avatar)
