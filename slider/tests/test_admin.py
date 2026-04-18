from django.test import TestCase
from django.contrib.admin.sites import site
from slider.models import SliderOne, SliderTwo
from slider.admin import SliderOneAdmin, SliderTwoAdmin

class SliderAdminTest(TestCase):
    def test_slider_one_admin_registered(self):
        self.assertIn(SliderOne, site._registry)
        self.assertIsInstance(site._registry[SliderOne], SliderOneAdmin)

    def test_slider_two_admin_registered(self):
        self.assertIn(SliderTwo, site._registry)
        self.assertIsInstance(site._registry[SliderTwo], SliderTwoAdmin)
