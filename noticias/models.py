from django.db import models

# Create your models here.

class Imagen(models.Model):
    imagen_id = models.AutoField(primary_key=True)
    imagen = models.ImageField(blank=True, null=True, default = 'default.png')

    def __str__(self):
        return str(self.imagen_id)

class Noticia(models.Model):
    noticia_id = models.SlugField(primary_key=True)
    contenido = models.TextField(blank=True, null=True)
    titulo = models.CharField(blank=False, null=False, max_length=50)
    imagen = models.ForeignKey(Imagen, on_delete=models.SET_DEFAULT, default = 'default.png')

    def __str__(self):
        return self.titulo