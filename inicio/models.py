from django.db import models

class Computadora(models.Model):
    cpu = models.CharField(max_length=15)
    gpu = models.CharField(max_length=15)
    ram = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.cpu} {self.gpu} {self.ram}'