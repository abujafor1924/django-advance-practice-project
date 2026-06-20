from rest_framework.permissions import BasePermission
from .models import RoomParticipant


class IsRoomParticipant(BasePermission):
    def has_permission(self, request, view):
        room_id = view.kwargs.get('pk')

        return RoomParticipant.objects.filter(
            room_id=room_id,
            user=request.user
        ).exists()


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_staff