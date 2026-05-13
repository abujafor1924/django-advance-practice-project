from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from package.models import CollaborationsCompany, Package

class CollaborationsCompanyModelTest(TestCase):
    def setUp(self):
        self.image = SimpleUploadedFile(
            name='test_icon.png',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/png'
        )
        self.company = CollaborationsCompany.objects.create(
            name="Test Company",
            icon=self.image
        )

    def test_company_creation(self):
        self.assertEqual(self.company.name, "Test Company")
        self.assertTrue(self.company.icon.name.startswith('collaborations/test_icon'))

    def test_company_str_representation(self):
        self.assertEqual(str(self.company), "Test Company")

class PackageModelTest(TestCase):
    def setUp(self):
        self.image = SimpleUploadedFile(
            name='package_icon.png',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/png'
        )
        self.package = Package.objects.create(
            name="Test Package",
            icon=self.image,
            details="Test details about the package",
            contact="1234567890"
        )

    def test_package_creation(self):
        self.assertEqual(self.package.name, "Test Package")
        self.assertEqual(self.package.details, "Test details about the package")
        self.assertEqual(self.package.contact, "1234567890")
        self.assertTrue(self.package.icon.name.startswith('package_icons/package_icon'))

    def test_package_str_representation(self):
        self.assertEqual(str(self.package), "Test Package")
