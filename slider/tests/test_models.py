from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from slider.models import SliderOne, SliderTwo

class SliderModelTest(TestCase):
    def setUp(self):
        # Create a small dummy image for testing
        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        self.dummy_image = SimpleUploadedFile(name='test_image.gif', content=image_content, content_type='image/gif')

    def test_slider_one_creation(self):
        slider_one = SliderOne.objects.create(image=self.dummy_image)
        self.assertTrue(isinstance(slider_one, SliderOne))
        self.assertEqual(str(slider_one), f"Slider One - {slider_one.id}")

    def test_slider_two_creation(self):
        slider_two = SliderTwo.objects.create(image=self.dummy_image)
        self.assertTrue(isinstance(slider_two, SliderTwo))
        self.assertEqual(str(slider_two), f"Slider Two - {slider_two.id}")
