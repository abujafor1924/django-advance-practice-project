from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from slider.models import SliderOne, SliderTwo

class SliderViewTests(APITestCase):
    def setUp(self):
        # Create a small dummy image for testing
        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        self.dummy_image = SimpleUploadedFile(name='test_image.gif', content=image_content, content_type='image/gif')
        
        # Create initial data
        self.slider1 = SliderOne.objects.create(image=self.dummy_image)
        self.slider2 = SliderTwo.objects.create(image=self.dummy_image)

    def test_slider_one_list(self):
        url = reverse('slider-one-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check 'results' because of pagination
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['count'], 1)

    def test_slider_one_detail(self):
        url = reverse('slider-one-detail', args=[self.slider1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.slider1.id)

    def test_slider_two_list(self):
        url = reverse('slider-two-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check 'results' because of pagination
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['count'], 1)

    def test_slider_two_detail(self):
        url = reverse('slider-two-detail', args=[self.slider2.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.slider2.id)

    def test_slider_one_not_found(self):
        url = reverse('slider-one-detail', args=[999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
