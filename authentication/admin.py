from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('phone_number', 'name', 'email', 'district', 'is_verified', 'is_staff', 'is_active')
    list_filter = ('district', 'is_verified', 'is_staff', 'is_superuser', 'is_active')
    
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('name', 'email', 'district')}),
        ('Permissions', {'fields': ('is_verified', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'created_at', 'updated_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password', 'name', 'email', 'district', 'is_verified'),
        }),
    )
    
    search_fields = ('phone_number', 'name', 'email')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')
