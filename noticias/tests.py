from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .views import Noticia, Edit, Add

# Create your tests here.


class TestUrls(SimpleTestCase):
    def test_noticia(self):
        url = reverse("noticias:noticia", kwargs={'_noticia_id':"Cebollitas_llega_a_primera_division"})
        self.assertEqual(resolve(url).func, Noticia)


    def test_edit(self):
        url = reverse("noticias:edit", kwargs={'_noticia_id':"Cebollitas_llega_a_primera_division"})
        self.assertEqual(resolve(url).func, Edit)

    def test_add(self):
        url = reverse("noticias:add")
        self.assertEqual(resolve(url).func, Add)
