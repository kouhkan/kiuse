from django.urls import path, include

from apps.interviews.views import (CreateInterviewView,
                                   UserInterviewView,
                                   UpdateInterviewView,
                                   ListInterviews, detail_interview,
                                   )

app_name = "interviews"

urlpatterns = [
    path(
        "interview",
        include([
            path("create/", CreateInterviewView.as_view(), name="create"),
            path("<pk>/", UserInterviewView.as_view(), name="user"),
            path("edit/<pk>/", UpdateInterviewView.as_view(), name="update"),
        ])
    ),
    path("", ListInterviews.as_view(), name="index"),
]
