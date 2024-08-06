from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'name@example.com'
        }),
        error_messages={
            'required': 'โปรดกรอกอีเมลของคุณ',
            'invalid': 'โปรดกรอกอีเมลที่ถูกต้อง'
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'ชื่อผู้ใช้งาน'
        })
        self.fields['username'].error_messages.update({
            'required': 'โปรดกรอกชื่อผู้ใช้งานของคุณ',
            'unique': 'ชื่อผู้ใช้งานนี้ถูกใช้ไปแล้ว'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'รหัสผ่าน'
        })
        self.fields['password1'].error_messages.update({
            'required': 'โปรดกรอกรหัสผ่าน',
            'min_length': 'รหัสผ่านต้องมีอย่างน้อย 8 ตัวอักษร'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'ยืนยันรหัสผ่าน'
        })
        self.fields['password2'].error_messages.update({
            'required': 'โปรดยืนยันรหัสผ่านของคุณ',
            'password_mismatch': 'รหัสผ่านไม่ตรงกัน'
        })

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "รหัสผ่านทั้งสองไม่ตรงกัน",
                code='password_mismatch',
            )
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "อีเมลนี้ถูกใช้ไปแล้ว",
                code='email_exists'
            )
        return email

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if not username or not email or not password1 or not password2:
            raise forms.ValidationError(
                "โปรดกรอกข้อมูลให้ครบถ้วน",
                code='incomplete'
            )
