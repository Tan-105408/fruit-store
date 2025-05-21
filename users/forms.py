# users/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Tên đăng nhập', max_length=100)
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Mật khẩu')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Xác nhận mật khẩu')
    full_name = forms.CharField(max_length=100, label='Họ và tên')
    birthdate = forms.DateField(label='Ngày sinh', widget=forms.DateInput(attrs={'type': 'date'}))
    phone = forms.CharField(max_length=15, label='Số điện thoại')
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ['username', 'password', 'confirm_password', 'full_name', 'birthdate', 'phone', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise ValidationError("Mật khẩu không khớp!")
