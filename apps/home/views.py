from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.interviews.models import Interview


class IndexView(ListView):
    template_name = "home/index.html"
    model = Interview
    queryset = Interview.objects.filter(approve=True)
    paginate_by = 25
    context_object_name = "interviews"


class InterviewDetailView(DetailView):
    template_name = "home/detail.html"
    model = Interview
    context_object_name = "interview"
