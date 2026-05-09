from django import forms
from .models import TopDoctor

class TopDoctorForm(forms.ModelForm):
    class Meta:
        model = TopDoctor
        fields = ['name', 'image', 'designations', 'experience', 'fees']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'designations': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'experience': forms.TextInput(attrs={'class': 'w-full p-2 border rounded'}),
            'fees': forms.NumberInput(attrs={'class': 'w-full p-2 border rounded'}),
        }
