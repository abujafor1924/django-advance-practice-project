from django.contrib import admin
from .models import (
	Room,
	RoomParticipant,
	DoctorProfile,
	UserProfile,
)


class RoomParticipantInline(admin.TabularInline):
	model = RoomParticipant
	extra = 0
	readonly_fields = ('assigned_at',)
	fields = ('user', 'role', 'assigned_by', 'assigned_at')
	autocomplete_fields = ('user',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
	list_display = ('room_name', 'created_by', 'created_at')
	search_fields = ('room_name',)
	inlines = (RoomParticipantInline,)

	def save_model(self, request, obj, form, change):
		# Ensure created_by is set to the admin creating the room when created via admin
		if not change or not obj.created_by:
			obj.created_by = request.user
		super().save_model(request, obj, form, change)

	def save_formset(self, request, form, formset, change):
		instances = formset.save(commit=False)
		for obj in instances:
			if not obj.assigned_by:
				obj.assigned_by = request.user
			obj.save()
		formset.save_m2m()


@admin.register(RoomParticipant)
class RoomParticipantAdmin(admin.ModelAdmin):
	list_display = ('room', 'user', 'role', 'assigned_by', 'assigned_at')
	list_filter = ('role',)
	search_fields = ('room__room_name', 'user__phone_number', 'user__email')
	autocomplete_fields = ('room', 'user')


@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'specialty', 'created_at')
	search_fields = ('user__phone_number', 'user__email', 'specialty')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'created_at')
	search_fields = ('user__phone_number', 'user__email')
