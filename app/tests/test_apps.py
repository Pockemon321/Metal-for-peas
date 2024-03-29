from django.test import TestCase
from django.apps import apps
from app.apps import AppConfig

class AppConfigTest(TestCase):
    def test_app_config(self):
        # Получаем конфигурацию приложения по его имени
        self.assertEqual(AppConfig.name, 'app')
        self.assertEqual(apps.get_app_config('app').name, 'app')

        # Проверяем значение default_auto_field
        self.assertEqual(AppConfig.default_auto_field, 'django.db.models.BigAutoField')