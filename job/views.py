from django.shortcuts import render
from .models import Job

# Create your views here.

def job_list(request):
    jop_list = Job.objects.all()
    context = {'jobs': jop_list}
    return render(request,'job/job_list',context)


def job_detail(request, id):
    job_detail = Job.objects.get(id=id)
    context = {'jobs': job_detail}
    return render(request,'job/job_detail.html',context)