from django.urls import path

from apps.interviews.views import (CreateInterviewView,
                                   UserInterviewView,
                                   UpdateInterviewView)


app_name = "interviews"

urlpatterns = [
    path("", CreateInterviewView.as_view(), name="create"),
    path("<pk>/", UserInterviewView.as_view(), name="detail"),
    path("edit/<pk>/", UpdateInterviewView.as_view(), name="update"),
]
