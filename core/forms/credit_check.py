from django import forms
from core.models import LocationNotMember

class LocationNotMemberForm(forms.ModelForm):
    class Meta:
        model = LocationNotMember
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ชื่อ'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'นามสกุล'}),
        }
        labels = {
            'first_name': 'ชื่อ',
            'last_name': 'นามสกุล',
        }
