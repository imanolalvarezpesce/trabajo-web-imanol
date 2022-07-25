from pickletools import read_unicodestringnl
from django.contrib import admin
from .models import Servicio

#register your models here

class ServicioAdmin(admin.ModelAdmin):
   readonly_filds =("created" , "updated")
  
admin.site.register(Servicio,ServicioAdmin)