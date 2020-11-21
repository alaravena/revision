from django.contrib import admin
from .models import Suscriptor, Galeria, Categoria, Producto, Promociones_Inicio, Promociones_Productos
# Register your models here.
class SuscriptoresAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'contraseña']
    search_fields = ['email']
    list_per_page = 10

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ['imagen']
    list_per_page = 10

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['email']
    list_per_page = 10

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'categoria', 'stock', 'caracteristica_1', 'caracteristica_2', 'caracteristica_3', 'caracteristica_4', 'caracteristica_5', 'imagen']
    search_fields = ['nombre']
    list_per_page = 10

class PromocionesInicioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'imagen']
    list_per_page = 10

class PromocionesProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'imagen']
    list_per_page = 10

admin.site.register(Suscriptor, SuscriptoresAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductosAdmin)
admin.site.register(Promociones_Inicio, PromocionesInicioAdmin)
admin.site.register(Promociones_Productos, PromocionesProductosAdmin)