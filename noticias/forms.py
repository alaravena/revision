from django import forms
from . import models
from django.utils.translation import gettext, gettext_lazy as _

class Noticia(forms.Form):
    noticia_id = forms.CharField(
        label=_("Slug de la noticia"),
        required=True,
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control pintar_form'}),
    )
    contenido = forms.CharField(
        label=_("Contenido"),
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control pintar_form'}), 
    )
    titulo = forms.CharField(
        label=_("Titulo"),
        strip=False,
        widget=forms.TextInput(attrs={'class': 'form-control pintar_form'}),
    )
    imagen = forms.ImageField(
        label=_("Imagen"),
        required = False,
        widget=forms.FileInput(attrs={'class': 'form-control pintar_form label_img'})
    )
    imagen_id = forms.IntegerField(
        label=_("ingrese ID Imagen"),
        required = False,
        widget=forms.TextInput(attrs={'class': 'form-control pintar_form'}),
    )
    class Meta:
        model = models.Noticia
        fields = ()