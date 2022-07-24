from django import forms

from apps.interviews.models import Interview


class CreateInterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        exclude = ("created_at", "updated_at", "approve", "tag", "user")
        labels = {
            "title": "یه عنوان مناسب برای مصاحبه‌ای که با خودت داری انجام میدی بنویس",
            "about": "در مورد خودت که کی هستی بنویس",
            "job": "چه کارهایی تا الان انجام دادی. الان مشغول به چی هستی؟",
            "gadget": "از چه سخت‌افزارهایی برای کار و استفاده روزمره استفاده میکنی؟",
            "software": "به‌طور کلی از چه نرم‌افزارهایی چه برای کار چه نرم‌افزارهایی که تو روزمره استفاده می‌کنی؟",
            "art": "کتاب فیلم موسیقی یا هر چیز دیگه؛ می‌پردازی به این چیزا؟",
        }


class UpdateInterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        exclude = ("created_at", "updated_at", "approve", "tag", "user")
        labels = {
            "title": "یه عنوان مناسب برای مصاحبه‌ای که با خودت داری انجام میدی بنویس",
            "about": "در مورد خودت که کی هستی بنویس",
            "job": "چه کارهایی تا الان انجام دادی. الان مشغول به چی هستی؟",
            "gadget": "از چه سخت‌افزارهایی برای کار و استفاده روزمره استفاده میکنی؟",
            "software": "به‌طور کلی از چه نرم‌افزارهایی چه برای کار چه نرم‌افزارهایی که تو روزمره استفاده می‌کنی؟",
            "art": "کتاب فیلم موسیقی یا هر چیز دیگه؛ می‌پردازی به این چیزا؟",
        }
