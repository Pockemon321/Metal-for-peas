from django.test import SimpleTestCase
from django.urls import reverse, resolve
from app.views import index, delivery, about, edit_product, delete_product

class UrlsTest(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_delivery_url_is_resolved(self):
        url = reverse('delivery')
        self.assertEquals(resolve(url).func, delivery)

    def test_about_url_is_resolved(self):
        url = reverse('about')
        self.assertEquals(resolve(url).func, about)

    def test_edit_product_url_is_resolved(self):
        url = reverse('edit_product', args=[1])
        self.assertEquals(resolve(url).func, edit_product)

    def test_delete_product_url_is_resolved(self):
        url = reverse('delete_product', args=[1])
        self.assertEquals(resolve(url).func, delete_product)