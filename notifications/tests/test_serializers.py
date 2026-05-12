from django.test import TestCase
from ..models import QuoteWiserd
from ..serializers import QuoteWiserdSerializer

class QuoteWiserdSerializerTest(TestCase):
    def setUp(self):
        QuoteWiserd.objects.all().delete()
        self.quote = QuoteWiserd.objects.create(title='Test Title', quote='Test Quote')
        self.serializer = QuoteWiserdSerializer(instance=self.quote)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id', 'title', 'quote', 'created_at']))

    def test_title_field_content(self):
        data = self.serializer.data
        self.assertEqual(data['title'], self.quote.title)
