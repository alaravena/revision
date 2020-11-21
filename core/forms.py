from django import forms
from django.forms import ModelForm
from .models import Producto, Galeria, Categoria, Promociones_Inicio, Promociones_Productos
from django.contrib.auth.forms import UserCreationForm
from django .contrib.auth.models import User
from django.forms import ValidationError

class ProductoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=50, required=True)
    precio = forms.IntegerField(min_value=1, max_value=1500000, required=True)
    stock  = forms.IntegerField(min_value=1, max_value=1500000, required=True)
    caracteristica_1 = forms.CharField(min_length=0, max_length=300, required=False)
    caracteristica_2 = forms.CharField(min_length=0, max_length=300, required=False)
    caracteristica_3 = forms.CharField(min_length=0, max_length=300, required=False)
    caracteristica_4 = forms.CharField(min_length=0, max_length=300, required=False)
    caracteristica_5 = forms.CharField(min_length=0, max_length=300, required=False)
    imagen = forms.ImageField(required=True)

    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'categoria', 'stock', 'caracteristica_1', 'caracteristica_2', 'caracteristica_3', 'caracteristica_4', 'caracteristica_5', 'imagen']

class GaleriaForm(forms.ModelForm):
    imagen = forms.ImageField(required=True)
    nombre = forms.CharField(min_length=3, max_length=50, required=True)
    class Meta:
        model = Galeria
        fields = ['imagen', 'nombre']

class CategoriaForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50, required=True)

    """ def clean_categoria(self):
        catego = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(catego="Celulares").exists()

        if existe:
            raise ValidationError("Este nombre ya Existe")
        else:
            return catego """
    class Meta:
        model = Categoria
        fields = ['nombre']

class PromocionesInicioForm(forms.ModelForm):
    imagen = forms.ImageField(required=True)
    nombre = forms.CharField(min_length=3, max_length=50, required=True)
    class Meta:
        model = Promociones_Inicio
        fields = ['imagen', 'nombre']

class PromocionesProductoForm(forms.ModelForm):
    imagen = forms.ImageField(required=True)
    nombre = forms.CharField(min_length=3, max_length=50, required=True)
    class Meta:
        model = Promociones_Productos
        fields = ['imagen', 'nombre']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]