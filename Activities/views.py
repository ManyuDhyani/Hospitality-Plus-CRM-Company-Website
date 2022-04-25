import imp
from django.shortcuts import render
from .models import Activities

def activityDetail(request):
    trek = Activities.objects.first()
    print(trek.content)
    context={'trek':trek}
    return render(request, "activityDetail.html", context)