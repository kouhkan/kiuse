from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from apps.interviews.forms import CreateInterviewForm, UpdateInterviewForm
from apps.interviews.models import Interview


class UserInterviewView(DetailView):
    template_name = "interviews/detail.html"
    context_object_name = "interview"
    queryset = Interview.objects.filter(approve=True)


class CreateInterviewView(LoginRequiredMixin, CreateView):
    template_name = "interviews/index.html"
    model = Interview
    form_class = CreateInterviewForm
    success_url = reverse_lazy("users:index")

    def form_valid(self, form):
        instance = form.save(commit=False)
        setattr(instance, "user", self.request.user)
        return super().form_valid(form)


class UpdateInterviewView(LoginRequiredMixin, UpdateView):
    template_name = "interviews/update.html"
    model = Interview
    form_class = UpdateInterviewForm
    success_url = reverse_lazy("users:index")

    def form_valid(self, form):
        instance = form.save(commit=False)
        setattr(instance, "approve", False)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            return redirect(reverse_lazy("users:index"))
        return super().dispatch(request, *args, **kwargs)


class ListInterviews(ListView):
    template_name = "kiusebase/index.html"
    model = Interview
    queryset = Interview.objects.all()
    context_object_name = "interviews"


def detail_interview(request, id):
    interview = Interview.objects.get(pk=id)
    return render(request, "kiusebase.html", context={"interview": interview})
