from django.contrib import admin
from .models import SpecialCategory, SpecialHospital, SpecialDoctor, SpecialBooking, SpecialPayment

@admin.register(SpecialCategory)
class SpecialCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(SpecialHospital)
class SpecialHospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name', 'address')

@admin.register(SpecialDoctor)
class SpecialDoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'hospital', 'category')
    list_filter = ('hospital', 'category')
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
