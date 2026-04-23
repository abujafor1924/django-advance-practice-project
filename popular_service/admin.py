from django.contrib import admin
from .models import ServiceCategory, SubCategory, Hospital, Doctor, Booking, Payment

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'name', 'icon')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'designation', 'hospital', 'subcategory')
    list_filter = ('hospital', 'subcategory')
    search_fields = ('name', 'designation')
    fields = ('name', 'image', 'designation', 'hospital', 'subcategory', 'doctor_details', 'doctor_sedule', 'contact_details')

class PaymentInline(admin.StackedInline):
    model = Payment
    extra = 0
    can_delete = False

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_name', 'phone', 'doctor', 'date', 'time', 'status')
    list_filter = ('status', 'date', 'doctor')
    search_fields = ('patient_name', 'phone')
    inlines = [PaymentInline]

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'booking', 'transaction_id', 'payment_method', 'payment_status')
    list_filter = ('payment_method', 'payment_status')
    search_fields = ('transaction_id', 'booking__patient_name')
