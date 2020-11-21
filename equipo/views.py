from django.shortcuts import render

# Create your views here.

def Equipo(request):
    context = {}
    return render(request, "equipo/team.html", context)