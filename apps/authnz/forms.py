from django import forms

from .models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")
        labels = {
            "username": "نام کاربری",
            "email": "پست الکترونیکی",
            "password": "رمز عبور",
        }
        help_texts = {
            "username": "نام کاربری باید یکتا باشد",
        }


class SignInForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=150, label="نام کاربری")
    password = forms.CharField(min_length=8, max_length=150, widget=forms.PasswordInput, label=" رمز عبور")
