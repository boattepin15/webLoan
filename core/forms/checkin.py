from django import forms
from core.models import Checkin

class CheckinForm(forms.ModelForm):
    class Meta:
        model = Checkin
        fields = ['checkin']
        widgets = {
            'checkin': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
