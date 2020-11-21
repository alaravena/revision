from django.shortcuts import render, redirect
from . import models
from . import forms
from django.contrib.auth.decorators import permission_required
from django.db.models import Max, Count
# Create your views here.

def Noticias(request):
    noticias = models.Noticia.objects.all()
    context = {
        "noticias": noticias
    }
    return render(request, "noticias/Noticias.html", context)

def Noticia(request, _noticia_id):
    noticia = models.Noticia.objects.get(noticia_id = _noticia_id)
    context = {
        "noticia": noticia
    }
    return render(request, "noticias/Noticia.html", context)


@permission_required("is_superuser")
def Edit(request, _noticia_id):
    noticia = models.Noticia.objects.get(noticia_id = _noticia_id)
    if (request.method == "POST"):
        form = forms.Noticia(request.POST, request.FILES)
        
        if (request.POST['action'] == "Guardar"):
            form = forms.Noticia(request.POST, request.FILES)
            if (form.is_valid()):
                noticia.noticia_id = form.cleaned_data["noticia_id"]
                noticia.contenido = form.cleaned_data["contenido"]
                noticia.titulo = form.cleaned_data["titulo"]
                noticia.save()
                return redirect("noticias:index")
        elif (request.POST['action'] == "Borrar"):
            noticia.delete()
            return redirect("noticias:index")
    
    elif (request.method == "GET"):
        data = {
            "noticia_id": noticia.noticia_id, 
            "contenido": noticia.contenido, 
            "titulo": noticia.titulo,
            "imagen": noticia.imagen,
            }
        form = forms.Noticia(initial=data)
        # form = forms.Noticia(initial=data2)
    context = {
        "noticia": noticia,
        "form": form
    }
    return render(request, "noticias/editnoticias.html", context)
            

@permission_required("is_superuser")
def Add(request):
    if (request.method == "GET"):
        args = models.Imagen.objects.annotate(n_noti=Count('imagen_id'))
        x=0
        for  args in args:
            x=x+1
        x=x+1
        data = {
            "imagen_id": x
        }
        _form = forms.Noticia(initial=data)

    elif (request.method == "POST"):
        _instance = models.Noticia()
        _instance2 = models.Imagen()
        _form = forms.Noticia(request.POST, request.FILES)
        
        if (_form.is_valid()):
            if (_form.cleaned_data['imagen']):
                _instance2.imagen_id = _form.cleaned_data["imagen_id"]
                _instance2.imagen = _form.cleaned_data["imagen"]
                _instance2.save()
                _instance.imagen = _form.cleaned_data["imagen"]
            else:
                img = models.Imagen.objects.get(imagen_id = _form.cleaned_data["imagen_id"])
                _instance.imagen = img
            _instance.noticia_id = _form.cleaned_data["noticia_id"]
            _instance.contenido = _form.cleaned_data["contenido"]
            _instance.titulo = _form.cleaned_data["titulo"]
            _instance.save()
            
            return redirect("noticias:index")
    context = {
            "form": _form
        }
    return render(request, "noticias/addnoticias.html", context)