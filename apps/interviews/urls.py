from django.urls import path

from apps.interviews.views import CreateInterviewView, UserInterviewView


app_name = "interviews"

urlpatterns = [
    path("", CreateInterviewView.as_view(), name="create"),
    path("<pk>/", UserInterviewView.as_view(), name="detail"),
]
