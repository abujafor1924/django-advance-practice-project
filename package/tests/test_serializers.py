from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from package.models import CollaborationsCompany, Package
from package.serializers import CollaborationsCompanySerializer, PackageSerializer

class CollaborationsCompanySerializerTest(TestCase):
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

    def test_serializer_output(self):
        serializer = CollaborationsCompanySerializer(instance=self.company)
        data = serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'icon', 'created_at'})
        self.assertEqual(data['name'], "Test Company")

class PackageSerializerTest(TestCase):
    def setUp(self):
        self.image = SimpleUploadedFile(
            name='package_icon.png',
            content=b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b',
            content_type='image/png'
        )
        self.package = Package.objects.create(
            name="Test Package",
            icon=self.image,
            details="Test details",
            contact="123456"
        )

    def test_serializer_output(self):
        serializer = PackageSerializer(instance=self.package)
        data = serializer.data
        self.assertEqual(set(data.keys()), {'id', 'name', 'icon', 'details', 'contact', 'created_at'})
        self.assertEqual(data['name'], "Test Package")
        self.assertEqual(data['details'], "Test details")
        self.assertEqual(data['contact'], "123456")
