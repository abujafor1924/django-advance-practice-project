from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from video_rooms.models import Room, RoomParticipant

User = get_user_model()


class TestVideoRoomsAPI(APITestCase):
    def setUp(self):
        # Create admin, doctor and normal user
        self.admin = User.objects.create_superuser(phone_number='+100', password='adminpass')
        self.doctor = User.objects.create_user(phone_number='+101', password='docpass')
        self.user = User.objects.create_user(phone_number='+102', password='userpass')

    def obtain_token(self, phone_number, password):
        # Adapt this if your project uses a different token endpoint or payload
        resp = self.client.post('/api/v1/auth/login/', {'phone_number': phone_number, 'password': password}, format='json')
        # Accept either 'access' or common keys
        return resp.data.get('access') or resp.data.get('token') or resp.data.get('access_token')

    def auth_client(self, user, password):
        token = self.obtain_token(user.phone_number, password)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

    def test_full_flow(self):
        # Admin creates room
        self.auth_client(self.admin, 'adminpass')
        resp = self.client.post('/api/v1/video-rooms/rooms/', {'room_name': 'r1'}, format='json')
        assert resp.status_code == 201, resp.data
        room_id = resp.data['id']

        # Admin assigns doctor and user
        resp = self.client.post(f'/api/v1/video-rooms/rooms/{room_id}/assign/', {'user_id': self.doctor.id, 'role': 'doctor'}, format='json')
        assert resp.status_code in (200, 201), resp.data
        resp = self.client.post(f'/api/v1/video-rooms/rooms/{room_id}/assign/', {'user_id': self.user.id, 'role': 'user'}, format='json')
        assert resp.status_code in (200, 201), resp.data

        # Doctor can list and request token
        self.auth_client(self.doctor, 'docpass')
        resp = self.client.get('/api/v1/video-rooms/rooms/my-rooms/')
        assert resp.status_code == 200, resp.data
        resp = self.client.get(f'/api/v1/video-rooms/rooms/{room_id}/token/')
        assert resp.status_code == 200, resp.data
        assert 'token' in resp.data or 'access_token' in resp.data

        # Unassigned user cannot get token
        other = User.objects.create_user(phone_number='+199', password='nopass')
        token = self.obtain_token(other.phone_number, 'nopass')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        resp = self.client.get(f'/api/v1/video-rooms/rooms/{room_id}/token/')
        assert resp.status_code == 403
