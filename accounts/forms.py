from django import forms
from .models import AlumniProfile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = AlumniProfile
        fields = ['profile_pic']
