from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Role

# Create your views here.

def role_index(request):
    all_data = Role.objects.all()
    if (len(all_data)==0):
        status = False
    else:
        status = True
    data = {'all_data':all_data, 'status':status}
    return render(request, 'admin/role.html', data)

def insert(request):
    if request.method == 'POST':
        role = request.POST.get('name')
        if(len(role)==0):
            return HttpResponse('name cannot be null!')
        else:
            all_data = Role(name=role)
            all_data.save()
    return redirect('index')

def edit(request):
    all_data = Role.objects.all()
    data = {'user_data': all_data}
    return render(request, 'admin/role.html', data)

def update(request,id):
     if request.method == 'POST':
        name = request.POST.get('name')

        obj = Role(
            id = id,
            name = name
        )
        obj.save()
        return redirect('index')
     return render(request, 'admin/role.html')

def delete(request, id):
    all_data = Role.objects.filter(id=id) #select single data by id from user model
    all_data.delete()
    return redirect('index')