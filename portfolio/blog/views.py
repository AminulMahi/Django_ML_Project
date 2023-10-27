from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request, 'blog.html')

def upload(request):
    return render(request, 'blog_upload.html')