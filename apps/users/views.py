from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.interviews.models import Interview


@login_required
def index(request):
    interview = Interview.objects.filter(user=request.user).first()
    return render(request, "users/index.html", context={"interview": interview})
