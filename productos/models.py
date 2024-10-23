from django.db import models

class Paleta(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    fecha = models.DateField()
    
    def __str__(self):
        return f'{self.id} {self.modelo}'