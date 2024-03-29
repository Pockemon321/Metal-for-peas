from django.test import TestCase
from app.models import Product

class ProductModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем объект для тестирования
        Product.objects.create(title='Тестовый товар', material='Дерево', price=1000, count=5, produced='Россия')

    def test_title_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'Название')

    def test_material_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('material').verbose_name
        self.assertEqual(field_label, 'Материал')

    def test_price_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('price').verbose_name
        self.assertEqual(field_label, 'Цена')

    def test_count_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('count').verbose_name
        self.assertEqual(field_label, 'Количество')

    def test_produced_label(self):
        product = Product.objects.get(id=1)
        field_label = product._meta.get_field('produced').verbose_name
        self.assertEqual(field_label, 'Произведён')

    def test_str_method(self):
        product = Product.objects.get(id=1)
        expected_object_name = f'{product.title} {product.price}'
        self.assertEqual(str(product), expected_object_name)

    def test_verbose_name(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product._meta.verbose_name, 'Товар')

    def test_verbose_name_plural(self):
        product = Product.objects.get(id=1)
        self.assertEqual(product._meta.verbose_name_plural, 'Товары')