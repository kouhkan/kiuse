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
