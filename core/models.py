from django.db import models

# Create your models here.
class Suscriptor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    contraseña = models.CharField(max_length=10)

    def __str__(self):
        return self.email

class Galeria(models.Model):
    imagen = models.ImageField(null=True, blank=True, upload_to ='galeria/')
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField()
    caracteristica_1 = models.CharField(max_length=200)
    caracteristica_2 = models.CharField(max_length=200)
    caracteristica_3 = models.CharField(max_length=200)
    caracteristica_4 = models.CharField(max_length=200)
    caracteristica_5 = models.CharField(max_length=200)
    imagen = models.ImageField(null=True, blank=True, upload_to='productos/')

    def __str__(self):
        return self.nombre

class Promociones_Inicio(models.Model):
    imagen = models.ImageField(null=True, blank=True, upload_to ='promociones_inicio/')
    nombre = models.CharField(max_length=80)
    def __str__(self):
        return self.nombre

class Promociones_Productos(models.Model):
    imagen = models.ImageField(null=True, blank=True, upload_to ='promociones_productos/')
    nombre = models.CharField(max_length=80)
    def __str__(self):
        return self.nombre