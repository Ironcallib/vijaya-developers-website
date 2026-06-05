from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Enquiry, Project, Service

def home(request):

    # Handle form submission
    if request.method == "POST":
        Enquiry.objects.create(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        messages.success(request, "Thank you! Your enquiry has been submitted successfully.")
        return redirect('home')

    # Load page data
    services = Service.objects.all()
    projects = Project.objects.all()

    return render(request, 'home.html', {
        'services': services,
        'projects': projects
    })
from django.http import HttpResponse
from django.contrib.auth import get_user_model

def create_admin(request):
    User = get_user_model()

    if not User.objects.filter(username="VijayaAdmin").exists():
        User.objects.create_superuser(
            username="VijayaAdmin",
            email="admin@example.com",
            password="Admin@123"
        )

    return HttpResponse("Admin created")