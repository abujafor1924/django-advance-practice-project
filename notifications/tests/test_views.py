from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import QuoteWiserd

class QuoteWiserdViewTest(APITestCase):
    def setUp(self):
        QuoteWiserd.objects.all().delete()
        self.quote = QuoteWiserd.objects.create(title='Test Title', quote='Test Quote')
        self.list_url = reverse('quote-wiserd-list')
        self.detail_url = reverse('quote-wiserd-detail', kwargs={'pk': self.quote.pk})

    def test_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_detail_view(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.quote.title)
