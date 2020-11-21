from django.urls import path
from . import views

app_name='nosotros'

urlpatterns = [
    path('', views.Nosotros, name="index"),
]