
# Create your views here.

from django.shortcuts import render
from .models import Enquiry
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import render
from .models import Project, Service
def home(request):
    if request.method == "POST":
        Enquiry.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        messages.success(request, "Thank you! Your enquiry has been submitted successfully.")
        return redirect('home')   # avoids duplicate submit

    return render(request, 'home.html')


def home(request):
    # Fetch all services and projects
    services = Service.objects.all()
    projects = Project.objects.all()
    
    return render(request, 'home.html', {
        'services': services,
        'projects': projects
    })