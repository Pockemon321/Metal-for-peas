from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from app.models import Product
from app.admin import ProductAdmin

class MockRequest:
    pass

class MockSuperUser:
    def has_perm(self, perm):
        return True

request = MockRequest()
request.user = MockSuperUser()

class TestProductAdmin(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_product_admin(self):
        # Создаем экземпляр ProductAdmin и проверяем его наличие в админ-панели
        admin = ProductAdmin(Product, self.site)
        self.assertTrue(isinstance(admin, ProductAdmin), "Should be an instance of ProductAdmin")
        self.assertTrue(admin.has_add_permission(request), "Superuser should have add permission")
        self.assertTrue(admin.has_change_permission(request), "Superuser should have change permission")
        self.assertTrue(admin.has_delete_permission(request), "Superuser should have delete permission")