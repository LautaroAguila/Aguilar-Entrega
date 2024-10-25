from django.db import models


class Notebook(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    fecha = models.DateField()
    imagen = models.ImageField(upload_to='img_notebook',blank=True, null=True)
    
    def __str__(self):
        return f' {self.id} {self.modelo}'
    
class Computadora(models.Model):
    nombre = models.CharField(max_length=20)
    cpu = models.CharField(max_length=20)
    gpu = models.CharField(max_length=20)
    ram = models.IntegerField()
    imagen = models.ImageField(upload_to='img_computadora',blank=True, null=True)
    
    def __str__(self):
        return f' {self.nombre}'