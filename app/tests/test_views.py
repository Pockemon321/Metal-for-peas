from django.test import TestCase, RequestFactory
from django.urls import reverse
from app.views import index, delivery, about, edit_product, delete_product
from app.models import Product

class ViewsTestCase(TestCase):
    def setUp(self):
        # Создаем фабрику запросов
        self.factory = RequestFactory()
        # Добавляем тестовый товар в базу данных
        self.product = Product.objects.create(title='Тестовый товар', material='Металл', price=1000, count=10, produced='Россия')

    def test_index_view(self):
        # Создаем запрос
        request = self.factory.get('/')
        # Получаем ответ от представления
        response = index(request)
        # Проверяем код ответа
        self.assertEqual(response.status_code, 200)

    def test_delivery_view(self):
        request = self.factory.get('/delivery/')
        response = delivery(request)
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        request = self.factory.get('/about/')
        response = about(request)
        self.assertEqual(response.status_code, 200)

    def test_edit_product_view(self):
        # Создаем URL с использованием идентификатора товара
        url = reverse('edit_product', args=[self.product.id])
        request = self.factory.get(url)
        response = edit_product(request, self.product.id)
        # Проверяем, что происходит перенаправление
        self.assertEqual(response.status_code, 302)

    def test_delete_product_view(self):
        url = reverse('delete_product', args=[self.product.id])
        request = self.factory.get(url)
        response = delete_product(request, self.product.id)
        self.assertEqual(response.status_code, 302)