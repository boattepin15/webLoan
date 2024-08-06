from django import forms
from core.models import Slip


class SlipForm(forms.ModelForm):
    class Meta:
        model = Slip
        fields = ['slip_image', 'cost']
        widgets = {
            'slip_image': forms.FileInput(attrs={'class': 'form-control'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
        }