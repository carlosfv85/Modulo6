from django.contrib import admin
from .models import Vehiculo

 
 
@admin.register(Vehiculo)
class VehiculoAdmin(admin.ModelAdmin):
    search_fields = ['marca', 'modelo']
    list_display = ['marca', 'modelo', 'serial_carroceria', 'serial_motor']
    ordering = ['fecha_creacion']  #Para eligir como se ordenan los datos en el panel de control
    list_filter = ['marca']