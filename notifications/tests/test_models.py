from django.test import TestCase
from ..models import QuoteWiserd

class QuoteWiserdModelTest(TestCase):
    def setUp(self):
        QuoteWiserd.objects.all().delete()
        self.quote = QuoteWiserd.objects.create(title='Test Title', quote='Test Quote')

    def test_quote_wiserd_creation(self):
        self.assertTrue(isinstance(self.quote, QuoteWiserd))
        self.assertEqual(str(self.quote), self.quote.title)
