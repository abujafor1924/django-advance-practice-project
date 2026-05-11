from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Appointment, Payment

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

class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 0
    can_delete = False

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'patient_phone', 'service_type', 'appointment_date', 'appointment_time', 'status', 'user')
    list_filter = ('status', 'service_type', 'appointment_date')
    search_fields = ('patient_name', 'patient_phone', 'user__phone_number')
    inlines = [PaymentInline]
    readonly_fields = ('created_at',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'transaction_id', 'amount', 'method', 'status', 'created_at')
    list_filter = ('status', 'method', 'created_at')
    search_fields = ('transaction_id', 'appointment__patient_name')
    readonly_fields = ('created_at',)
