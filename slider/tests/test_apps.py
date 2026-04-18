from django.test import TestCase
from slider.apps import SliderConfig
from django.apps import apps

class SliderConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(SliderConfig.name, 'slider')
        self.assertEqual(apps.get_app_config('slider').name, 'slider')
