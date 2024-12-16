from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    MARCAS =  [("Fiat", "Fiat"), ("Chevrolet", "Chevrolet"), ("Ford", "Ford"), ("Toyota","Toyota"),]
    CATEGORIAS =  [("Particular", "Particular"), ("Transporte", "Transporte"), ("Carga","Carga"),]

    marca =  models.CharField(max_length=20, blank=False, null=False, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100, blank=False, null=False)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, blank=False, null=False, choices=CATEGORIAS, default="Particular")
    precio = models.PositiveIntegerField(default = 999999999,blank=False, null=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now = True)

    def condicion_precio(self):
        if self.precio <=10000:
            return "Bajo"
        
        elif 10000< self.precio <=30000:
            return "Medio"
        
        else:
            return "Alto"
    
    class Meta:
        permissions = [('visualizar_catalogo', 'Puede visualizar catalogo')]