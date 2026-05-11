from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Appointment, Payment

class AppointmentInline(admin.TabularInline):
    model = Appointment
    extra = 0
    fields = ('patient_name', 'appointment_date', 'appointment_time', 'status', 'service_type')
    readonly_fields = ('patient_name', 'appointment_date', 'appointment_time', 'service_type')
    show_change_link = True

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('phone_number', 'name', 'email', 'district', 'is_verified', 'is_staff', 'is_active')
    list_filter = ('district', 'is_verified', 'is_staff', 'is_superuser', 'is_active')
    inlines = [AppointmentInline]
    
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
    list_display = ('id', 'patient_name', 'patient_phone', 'get_doctor', 'service_type', 'appointment_date', 'appointment_time', 'status', 'user')
    list_filter = ('status', 'service_type', 'appointment_date', 'created_at')
    search_fields = ('patient_name', 'patient_phone', 'user__phone_number')
    list_editable = ('status',)
    date_hierarchy = 'appointment_date'
    inlines = [PaymentInline]
    readonly_fields = ('service_type', 'created_at')

    def get_doctor(self, obj):
        return str(obj.service_object)
    get_doctor.short_description = 'Doctor'

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'transaction_id', 'amount', 'method', 'status', 'created_at')
    list_filter = ('status', 'method', 'created_at')
    search_fields = ('transaction_id', 'appointment__patient_name')
    readonly_fields = ('created_at',)
