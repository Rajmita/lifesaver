
from django import forms
from .models import BloodPost

class BloodForm(forms.ModelForm):
    class Meta:
        model = BloodPost
        fields = ['name', 'blood_type', 'city', 'contact', 'message'] 




