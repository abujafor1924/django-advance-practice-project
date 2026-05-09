from django import forms
from .models import Doctor, Hospital, SubCategory

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'name', 'image', 'designation', 'years_of_experience', 
            'doctor_fees', 'hospital', 'subcategory', 
            'doctor_details', 'doctor_sedule', 'contact_details'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'designation': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'doctor_fees': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
            'hospital': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'subcategory': forms.Select(attrs={'class': 'w-full p-2 border rounded'}),
            'doctor_details': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 3}),
            'doctor_sedule': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 3}),
            'contact_details': forms.Textarea(attrs={'class': 'w-full p-2 border rounded', 'rows': 3}),
        }
