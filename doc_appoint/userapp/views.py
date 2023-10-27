from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Role

# Create your views here.

def role_index(request):
    return render(request, 'admin/role.html')
