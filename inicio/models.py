from django.db import models

class Auto(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    anio = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.marca} {self.modelo} {self.anio}'