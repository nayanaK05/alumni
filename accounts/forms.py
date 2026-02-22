from django import forms
from .models import AlumniProfile

class AlumniProfileForm(forms.ModelForm):
    class Meta:
        model = AlumniProfile
        fields = [
            'full_name',
            'department',
            'passout_year',
            'register_number',
            'phone',
            'current_job',
            'company',
            'profile_picture',
            'skills',
        ]
        widgets = {
            'skills': forms.CheckboxSelectMultiple()
        }