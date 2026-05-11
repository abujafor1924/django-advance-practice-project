from django.contrib import admin
from .models import SpecialDoctor, SpecialBooking, SpecialPayment

@admin.register(SpecialDoctor)
class SpecialDoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'hospital', 'subcategory', 'years_of_experience', 'doctor_fees')
    list_filter = ('hospital', 'subcategory')
    search_fields = ('name', 'designation')

@admin.register(SpecialBooking)
class SpecialBookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'doctor', 'date', 'time', 'status')
    list_filter = ('status', 'date')
    search_fields = ('patient_name', 'phone')

@admin.register(SpecialPayment)
class SpecialPaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'transaction_id', 'payment_method', 'payment_status')
    list_filter = ('payment_method', 'payment_status')
    search_fields = ('transaction_id',)
