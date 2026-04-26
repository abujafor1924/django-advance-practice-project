from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from medical_accessories.models import AccessoryCategory, MedicalAccessory

class AccessoryCategoryModelTest(TestCase):
    def setUp(self):
        self.image = SimpleUploadedFile(
            name='test_category.png',
            content=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82',
            content_type='image/png'
        )
        self.category = AccessoryCategory.objects.create(
            name="Test Category",
            image=self.image
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(str(self.category), "Test Category")

class MedicalAccessoryModelTest(TestCase):
    def setUp(self):
        self.category_image = SimpleUploadedFile(name='cat.png', content=b'content', content_type='image/png')
        self.category = AccessoryCategory.objects.create(name="Test Category", image=self.category_image)
        self.accessory_image = SimpleUploadedFile(name='acc.png', content=b'content', content_type='image/png')
        self.accessory = MedicalAccessory.objects.create(
            category=self.category,
            name="Test Accessory",
            image=self.accessory_image,
            details="Test Details",
            contact_details="Test Contact"
        )

    def test_accessory_creation(self):
        self.assertEqual(self.accessory.name, "Test Accessory")
        self.assertEqual(self.accessory.category, self.category)
        self.assertEqual(str(self.accessory), "Test Accessory")
