from django.shortcuts import render

# Create your views here.


def Home(request):
    context = {}
    return render(request, "Home.html", context)