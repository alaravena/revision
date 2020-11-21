from django.shortcuts import render
from .models import Suscriptor, Galeria, Producto, Promociones_Productos, Promociones_Inicio, Categoria
from .forms import ProductoForm, GaleriaForm, CategoriaForm, PromocionesInicioForm, PromocionesProductoForm, CustomUserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index (request):

    data = {
            'galerias':Galeria.objects.all(),
            'PromocionesInicio':Promociones_Inicio.objects.all()
        }   

    if request.method == 'POST':
        suscripto = Suscriptor()
        suscripto.nombre = request.POST.get('nombre')
        suscripto.apellido = request.POST.get('apellido')
        suscripto.email = request.POST.get('email')
        suscripto.contraseña = request.POST.get('password')

        try:
            messages.success(request, "Te haz Suscrito Correctamente")
            suscripto.save()
            return redirect('index')
        except:
            messages.error(request, "Error al Suscribirse")
            return redirect('index')
    return render(request,'core/index.html', data)

def compra (request):
    return render(request,'core/compra.html')

def productos (request):

    data = {
            'PromocionesProductos':Promociones_Productos.objects.all(),
            'Productos':Producto.objects.all()
        }
    return render(request,'core/productos.html', data)

@permission_required('core.add_categoria')
def categoriaAdmin (request):
    data = {
        'form':CategoriaForm(),
        'Categoria':Categoria.objects.all()
    }
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
            return redirect('categoriaAdmin')
    return render(request, 'core/categoriaAdmin.html', data)

@permission_required('core.add_galeria')
def galeriaAdmin (request):
    data = {
        'form':GaleriaForm(),
        'Galeria':Galeria.objects.all()
    }
    if request.method == 'POST':
        formulario = GaleriaForm(request.POST, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
            return redirect('galeriaAdmin')
                
    return render(request, 'core/galeriaAdmin.html', data)

@permission_required('core.add_productos')
def productosAdmin (request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    data = {
        'form':ProductoForm(),
        'entity':productos,
        'paginator':paginator
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
            return redirect('productosAdmin')
    return render(request, 'core/productosAdmin.html', data)

@permission_required('core.add_promociones_inicio')
def promocionesinicioAdmin (request):
    data = {
        'form':PromocionesInicioForm(),
        'promocionesInicio':Promociones_Inicio.objects.all()
    }
    if request.method == 'POST':
        formulario = PromocionesInicioForm(request.POST, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
            return redirect('promocionesinicioAdmin')
    return render(request, 'core/promocionesinicioAdmin.html', data)

@permission_required('core.add_promociones_productos')
def promocionesproductosAdmin (request):
    data = {
        'form':PromocionesProductoForm(),
        'promocionesProductos':Promociones_Productos.objects.all()
    }
    if request.method == 'POST':
        formulario = PromocionesProductoForm(request.POST, files=request.FILES)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, "Agregado Correctamente")
            return redirect('promocionesproductosAdmin')
    return render(request, 'core/promocionesproductosAdmin.html', data)

@login_required
@permission_required('core.add_productos')
def inicioAdmin (request):
    
    return render(request, 'core/inicioAdmin.html')

@permission_required('core.change_producto')
def modificarProductoAdmin(request, id):
    producto = Producto.objects.get(id=id)
    data = {
        'form':ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if  formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            data['form']= formulario
            return redirect('productosAdmin')
    return render(request, 'core/modificarProductoAdmin.html', data)

@permission_required('core.delete_producto')
def eliminarProducto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="productosAdmin")

@permission_required('core.delete_galeria')
def eliminarGaleria(request, id):
    galeria = Galeria.objects.get(id=id)
    galeria.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="galeriaAdmin")

@permission_required('core.delete_categoria')
def eliminarCategoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="categoriaAdmin")

@permission_required('core.delete_promocion_inicio')
def eliminarPromocionInicio(request, id):
    promoInicio = Promociones_Inicio.objects.get(id=id)
    promoInicio.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="promocionesinicioAdmin")

@permission_required('core.delete_promocion_producto')
def eliminarPromocionProducto(request, id):
    promoProducto = Promociones_Productos.objects.get(id=id)
    promoProducto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="promocionesproductosAdmin")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="index")
        data["form"] = formulario

    
    return render(request, 'registration/registro.html', data)

def test_disminuir_stock(stock):
    disminuir = stock - 1
    return disminuir