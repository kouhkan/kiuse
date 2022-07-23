from django.urls import path

from . import views

app_name = "authnz"

urlpatterns = [
       path("signup", views.SignUpView.as_view(), name="signup"),
       path("signin", views.signin_view, name="signin"),
]
