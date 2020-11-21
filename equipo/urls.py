from django.urls import path
from . import views

app_name='equipo'

urlpatterns = [
    path('', views.Equipo, name="index"),
]