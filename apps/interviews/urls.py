from django.urls import path

from apps.interviews.views import CreateInterviewView


app_name = "interviews"

urlpatterns = [
    path("", CreateInterviewView.as_view(), name="create"),
]
