from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from slider.serializers import SliderOneSerializer, SliderTwoSerializer
from rest_framework import serializers
from unittest.mock import MagicMock

class SliderSerializerTest(TestCase):
    def setUp(self):
        # Create a small dummy image for testing
        self.image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        self.valid_image = SimpleUploadedFile(name='test_image.gif', content=self.image_content, content_type='image/gif')

    def test_slider_one_serializer_valid_image(self):
        data = {'image': self.valid_image}
        serializer = SliderOneSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_slider_one_serializer_large_image(self):
        # Create a valid image but mock its size to be large
        large_image = SimpleUploadedFile(name='large_image.gif', content=self.image_content, content_type='image/gif')
        # We need to mock the size attribute because it's what the validator checks
        # Actually, SimpleUploadedFile has a .size property. 
        # But the validator in serializers.py uses value.size.
        
        # To bypass Pillow's validation but fail the size validation:
        # We can't easily mock .size on SimpleUploadedFile because it's often a property.
        # Let's just create a large enough valid image or mock the validator.
        # Alternatively, just use a large content that is still a valid image (e.g. large GIF)
        
        # A simpler way: mock the validator's check.
        # But we want to test the validator.
        
        # Let's try to just give it a large content and hope Pillow doesn't mind if it's just trailing zeros?
        # No, Pillow usually checks the whole file if it's a real image.
        
        # Let's just mock the 'size' on the file object passed to the serializer.
        large_image.size = 6 * 1024 * 1024 # 6MB
        
        data = {'image': large_image}
        serializer = SliderOneSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('image', serializer.errors)
        self.assertEqual(serializer.errors['image'][0], "Image file too large ( > 5MB )")

    def test_slider_two_serializer_valid_image(self):
        data = {'image': self.valid_image}
        serializer = SliderTwoSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_slider_two_serializer_large_image(self):
        large_image = SimpleUploadedFile(name='large_image.gif', content=self.image_content, content_type='image/gif')
        large_image.size = 6 * 1024 * 1024 # 6MB
        
        data = {'image': large_image}
        serializer = SliderTwoSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('image', serializer.errors)
        self.assertEqual(serializer.errors['image'][0], "Image file too large ( > 5MB )")
