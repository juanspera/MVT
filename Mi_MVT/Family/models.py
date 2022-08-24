from django.db import models

# Create your models here.
class Familia(models.Model):

    name = models.CharField(max_length=30)
    edad = models.PositiveIntegerField()
    fecha_nac = models.DateField()