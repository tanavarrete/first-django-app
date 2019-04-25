from django.db import models

# Create your models here.


class Pelicula(models.Model):
    titulo = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True, null=True)
    puntuacion = models.DecimalField(decimal_places=2, max_digits=1000)
