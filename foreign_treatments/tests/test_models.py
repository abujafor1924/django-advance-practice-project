from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from foreign_treatments.models import Country, Hospital, HospitalDetail

class CountryModelTest(TestCase):
    def setUp(self):
        self.flag = SimpleUploadedFile(
            name='test_flag.png',
            content=b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\x9cc\x00\x01\x00\x00\x05\x00\x01\r\n-\xb4\x00\x00\x00\x00IEND\xaeB`\x82',
            content_type='image/png'
        )
        self.country = Country.objects.create(
            name="Test Country",
            flag=self.flag
        )

    def test_country_creation(self):
        self.assertEqual(self.country.name, "Test Country")
        self.assertEqual(str(self.country), "Test Country")

class HospitalModelTest(TestCase):
    def setUp(self):
        self.flag = SimpleUploadedFile(name='test_flag.png', content=b'content', content_type='image/png')
        self.country = Country.objects.create(name="Test Country", flag=self.flag)
        self.icon = SimpleUploadedFile(name='test_icon.png', content=b'content', content_type='image/png')
        self.hospital = Hospital.objects.create(
            country=self.country,
            name="Test Hospital",
            icon=self.icon,
            public_hospital_count=5
        )

    def test_hospital_creation(self):
        self.assertEqual(self.hospital.name, "Test Hospital")
        self.assertEqual(self.hospital.country, self.country)
        self.assertEqual(str(self.hospital), "Test Hospital")

class HospitalDetailModelTest(TestCase):
    def setUp(self):
        self.flag = SimpleUploadedFile(name='test_flag.png', content=b'content', content_type='image/png')
        self.country = Country.objects.create(name="Test Country", flag=self.flag)
        self.icon = SimpleUploadedFile(name='test_icon.png', content=b'content', content_type='image/png')
        self.hospital = Hospital.objects.create(
            country=self.country,
            name="Test Hospital",
            icon=self.icon
        )
        self.banner = SimpleUploadedFile(name='test_banner.png', content=b'content', content_type='image/png')
        self.hospital_detail = HospitalDetail.objects.create(
            hospital=self.hospital,
            banner=self.banner,
            description="Test Description",
            contact_info="Test Contact Info"
        )

    def test_hospital_detail_creation(self):
        self.assertEqual(self.hospital_detail.hospital, self.hospital)
        self.assertEqual(self.hospital_detail.description, "Test Description")
        self.assertEqual(str(self.hospital_detail), f"Details for {self.hospital.name}")
