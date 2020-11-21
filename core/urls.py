from django.urls import path
from core.views import index, compra, productos, galeriaAdmin, productosAdmin, promocionesinicioAdmin, promocionesproductosAdmin, categoriaAdmin, inicioAdmin, modificarProductoAdmin, eliminarProducto, eliminarCategoria, eliminarGaleria, eliminarPromocionInicio, eliminarPromocionProducto, registro

urlpatterns = [
    path('', index,name="index"),
    path('productos/', productos,name="productos"),
    path('productos/compra/', compra,name="compra"),
    path('galeriaAdmin/', galeriaAdmin, name="galeriaAdmin"),
    path('productosAdmin/', productosAdmin,name="productosAdmin"),
    path('categoriaAdmin/', categoriaAdmin,name="categoriaAdmin"),
    path('promocionesinicioAdmin/', promocionesinicioAdmin,name="promocionesinicioAdmin"),
    path('promocionesproductosAdmin/', promocionesproductosAdmin,name="promocionesproductosAdmin"),
    path('inicioAdmin/', inicioAdmin, name="inicioAdmin"),
    path('modificarProductoAdmin/<id>/', modificarProductoAdmin, name="modificarProductoAdmin"),
    path('eliminarProducto/<id>/', eliminarProducto, name="eliminarProducto"),
    path('eliminarCategoria/<id>/', eliminarCategoria, name="eliminarCategoria"),
    path('eliminarGaleria/<id>/', eliminarGaleria, name="eliminarGaleria"),
    path('eliminarPromocionInicio/<id>/', eliminarPromocionInicio, name="eliminarPromocionInicio"),
    path('eliminarPromocionProducto/<id>/', eliminarPromocionProducto, name="eliminarPromocionProducto"),
    path('registro/', registro, name="registro"),
]
