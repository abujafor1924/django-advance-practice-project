from django.contrib import admin
from .models import TopDoctor, Booking, Payment

@admin.register(TopDoctor)
class TopDoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'years_of_experience', 'hospital', 'created_at')
    search_fields = ('name', 'designation', 'hospital__name')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor', 'appointment_date', 'appointment_time', 'status')
    list_filter = ('status', 'appointment_date')
    search_fields = ('patient_name', 'patient_phone', 'doctor__name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'payment_method', 'payment_status', 'transaction_id', 'amount')
    list_filter = ('payment_status', 'payment_method')
    search_fields = ('transaction_id', 'booking__patient_name')
