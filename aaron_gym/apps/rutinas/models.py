from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Cuerpo(models.Model):
    
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Rutina(models.Model):
    
    titulo = models.CharField(max_length = 150)
    cuerpo = models.ForeignKey(Cuerpo, on_delete = models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descripcion = models.TextField(null=True)
    file = models.FileField(upload_to='rutinas')
    img = models.ImageField(upload_to='videos',null=True)
    
    def __str__(self):
        return self.titulo