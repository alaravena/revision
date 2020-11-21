from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name='noticias'

urlpatterns = [
    path("add/", views.Add, name="add"),
    path('', views.Noticias, name="index"),
    path("edit/<str:_noticia_id>/", views.Edit, name="edit"),
    path("<str:_noticia_id>/", views.Noticia, name="noticia"),
]