from django.db import models
from django.conf import settings


class Categoria(models.Model):
    
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Cuerpo(models.Model):
    
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Video(models.Model):
    
    titulo = models.CharField(max_length = 150)
    cuerpo = models.ForeignKey(Cuerpo, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descripcion = models.TextField(null=True)
    url = models.URLField()
    img = models.ImageField(upload_to='videos',null=True)
    
    def __str__(self):
        return self.titulo