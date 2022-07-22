from django.urls import path

from . import views

app_name = "authnz"

urlpatterns = [
       path("", views.index, name="index"),
]
