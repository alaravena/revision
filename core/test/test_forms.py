from django.test import SimpleTestCase
from core.forms import ProductoForm, GaleriaForm, CategoriaForm, PromocionesInicioForm, PromocionesProductoForm, CustomUserCreationForm

class TestForms(SimpleTestCase):    
    
    def test_producto_form_valid_data(self):
        form = ProductoForm(data={
        'nombre': 'producto1',
        'precio': 10000,
        'stock': 12,
        'caracteristica_1': 'marca: samsung',
        'caracteristica_2': 'capacidad: 150gb', 
        'caracteristica_3': 'camara: 44mpx',
        'caracteristica_4': 'color: Rojo',
        'caracteristica_5': 'audifonos: si',
        })

        self.assertTrue(form.is_valid())

    def test_producto_form_no_data(self):
        form = ProductoForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 7)


""" consola ejecutar #python manage.py test core  """