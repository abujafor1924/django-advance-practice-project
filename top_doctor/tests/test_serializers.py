from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from top_doctor.models import TopDoctor
from top_doctor.serializers import TopDoctorSerializer

class TopDoctorSerializerTest(TestCase):
    def setUp(self):
        image_content = b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x4c\x01\x00\x3b'
        self.image = SimpleUploadedFile('test_image.gif', image_content, content_type='image/gif')
        self.doctor_data = {
            "name": "Dr. Smith",
            "designation": "Cardiologist",
            "years_of_experience": 10,
            "image": self.image
        }

    def test_top_doctor_serializer(self):
        serializer = TopDoctorSerializer(data=self.doctor_data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.data['name'], "Dr. Smith")
