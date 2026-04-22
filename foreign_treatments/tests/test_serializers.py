from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from foreign_treatments.models import Country, Hospital, HospitalDetail
from foreign_treatments.serializers import CountrySerializer, HospitalSerializer, HospitalDetailSerializer

class SerializerTest(TestCase):
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
        self.banner = SimpleUploadedFile(name='test_banner.png', content=b'content', content_type='image/png')
        self.hospital_detail = HospitalDetail.objects.create(
            hospital=self.hospital,
            banner=self.banner,
            description="Test Description",
            contact_info="Test Contact Info"
        )

    def test_country_serializer(self):
        serializer = CountrySerializer(instance=self.country)
        data = serializer.data
        self.assertEqual(data['name'], self.country.name)
        self.assertEqual(data['hospital_count'], 1)

    def test_hospital_serializer(self):
        serializer = HospitalSerializer(instance=self.hospital)
        data = serializer.data
        self.assertEqual(data['name'], self.hospital.name)
        self.assertEqual(data['public_hospital_count'], self.hospital.public_hospital_count)

    def test_hospital_detail_serializer(self):
        serializer = HospitalDetailSerializer(instance=self.hospital_detail)
        data = serializer.data
        self.assertEqual(data['description'], self.hospital_detail.description)
        self.assertEqual(data['hospital'], self.hospital.id)
