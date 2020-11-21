from django.shortcuts import render

# Create your views here.

def Nosotros(request):
    context = {}
    return render(request, "nosotros/nosotros.html", context)