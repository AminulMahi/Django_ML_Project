from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def user_index(request):
    return render(request, 'admin/user.html')
