from django import forms
from core.models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['phone_number', 'address_line', 'province', 'district', 'postal_code']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
        }
