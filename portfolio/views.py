from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.html import strip_tags
from .models import contact
from admin_app.models import blog

# Create your views here.

def home(request):
    return render(request, 'index.html')

def user_blog(request): # class name and function name cannot be same
    all_data = blog.objects.all()

    data = {
        'all_blog_data' : all_data,
        }
    return render(request, 'blog.html', data)

# def user_blog(request):
#     all_data = blog.objects.all()[:10]  # Retrieve all blog entries (limiting to 10 for optimization)
#     data_with_stripped_tags = []

#     for entry in all_data:
#         stripped_description = strip_tags(entry.description)  # Stripping HTML tags for the description
#         data_with_stripped_tags.append({
#             'title': entry.title,
#             'description': stripped_description,
#             'date': entry.date  # Assuming this field exists in the model
#         })

#     context = {
#         'all_blog_data': data_with_stripped_tags,
#     }
#     return render(request, 'blog.html', context)

def blog_details(request,id):
    blog_detail = blog.objects.get(id=id)
    
    data = {
        'blog_detail' : blog_detail,
    }
    return render(request, 'blog_details.html', data)

def contact_info(request):
    if request.method == 'POST':  # post is secure method
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contactus= contact(name=name,email=email,phone=phone,message=message)
        contactus.save()

        return redirect('home')