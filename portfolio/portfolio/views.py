from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import contact

# Create your views here.

def home(request):
    return render(request, 'index.html')

def contact_info(request):
    if request.method == 'POST':  # post is secure method
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contactus= contact(name=name,email=email,phone=phone,message=message)
        contactus.save()

        return redirect('home')