from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from medical_accessories.models import AccessoryCategory, MedicalAccessory
from medical_accessories.serializers import (
    AccessoryCategorySerializer,
    MedicalAccessoryListSerializer,
    MedicalAccessoryDetailSerializer
)

class SerializerTest(TestCase):
    def setUp(self):
        self.image = SimpleUploadedFile(name='test.png', content=b'content', content_type='image/png')
        self.category = AccessoryCategory.objects.create(name="Test Category", image=self.image)
        self.accessory = MedicalAccessory.objects.create(
            category=self.category,
            name="Test Accessory",
            image=self.image,
            details="Test Details",
            contact_details="Test Contact"
        )

    def test_category_serializer(self):
        serializer = AccessoryCategorySerializer(instance=self.category)
        self.assertEqual(serializer.data['name'], "Test Category")

    def test_accessory_list_serializer(self):
        serializer = MedicalAccessoryListSerializer(instance=self.accessory)
        self.assertEqual(set(serializer.data.keys()), {'id', 'name', 'image'})
        self.assertEqual(serializer.data['name'], "Test Accessory")

    def test_accessory_detail_serializer(self):
        serializer = MedicalAccessoryDetailSerializer(instance=self.accessory)
        self.assertEqual(serializer.data['name'], "Test Accessory")
        self.assertEqual(serializer.data['category_name'], "Test Category")
        self.assertEqual(serializer.data['details'], "Test Details")
