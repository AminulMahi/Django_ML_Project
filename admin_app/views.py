from django.shortcuts import render, redirect
from .models import blog

# Create your views here.

def admin(request):
    return render(request, 'admin/admin_index.html')

def admin_blog(request):
    all_data = blog.objects.all()
    data = {'all_blog_data' : all_data}
    return render(request, 'admin/admin_blog.html', data)


def insert_blog(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    date = request.POST.get('date')
    image = request.FILES.get('image')
    description = request.POST.get('description')
    # CreatingVariable = requestMethod.POSTmethod.GetMethod(ValueFromHTMLnameAttribute)

    blog_obj = blog(
        title = title,
        author = author,
        date = date,
        image = image,
        description = description
    )
    blog_obj.save()
    return redirect('admin_blog')

def delete_blog(request, id):
    all_data = blog.objects.filter(id=id) #select single data by id from user model
    all_data.delete()
    return redirect('admin_blog')