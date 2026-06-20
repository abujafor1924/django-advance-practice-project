

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.contrib.auth import get_user_model

from .models import Room, RoomParticipant
from .serializers import RoomSerializer, RoomCreateSerializer, RoomParticipantSerializer
from .agora import generate_agora_token
from .permissions import IsAdminUser


User = get_user_model()


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all().order_by('-created_at')
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create':
            return RoomCreateSerializer
        return RoomSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({'detail': 'Only admins can create rooms.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        room = serializer.save(created_by=request.user)
        return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='my-rooms')
    def my_rooms(self, request):
        rooms = Room.objects.filter(participants__user=request.user).distinct()
        return Response(RoomSerializer(rooms, many=True).data)

    @action(detail=True, methods=['post'], url_path='assign', permission_classes=[IsAdminUser])
    def assign(self, request, pk=None):
        room = self.get_object()
        user_id = request.data.get('user_id')
        role = request.data.get('role', RoomParticipant.ROLE_USER)

        if role not in dict(RoomParticipant.ROLE_CHOICES):
            return Response({'detail': 'Invalid role.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # configurable max participants per room (default: 2)
        max_participants = getattr(settings, 'VIDEO_ROOMS_MAX_PARTICIPANTS', 2)

        existing = RoomParticipant.objects.filter(room=room, user=user).first()
        if not existing:
            current_count = RoomParticipant.objects.filter(room=room).count()
            if current_count >= max_participants:
                return Response(
                    {'detail': f'Room already has maximum of {max_participants} participants.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            rp = RoomParticipant.objects.create(
                room=room,
                user=user,
                role=role,
                assigned_by=request.user
            )
            created = True
        else:
            # update role/assigned_by if participant already exists
            existing.role = role
            existing.assigned_by = request.user
            existing.save()
            rp = existing
            created = False

        return Response(RoomParticipantSerializer(rp).data)

    @action(detail=True, methods=['get'], url_path='token')
    def token(self, request, pk=None):
        room = self.get_object()
        # Only assigned participants may obtain a token.
        is_participant = RoomParticipant.objects.filter(room=room, user=request.user).exists()
        if not is_participant:
            return Response({'detail': 'Not assigned to this room.'}, status=status.HTTP_403_FORBIDDEN)

        # Do not expose or bind uid in the API response; generate a token for uid=0
        token = generate_agora_token(room.room_name, uid=0)

        return Response({
            'app_id': getattr(settings, 'AGORA_APP_ID', ''),
            'channel': room.room_name,
            'token': token
        })