from django.shortcuts import redirect, render
from django.urls import reverse
from .models import UserView
from django.contrib.auth.models import User
from .forms import UserForms,UserCreate

from django.contrib import messages
# Create your views here.

def dash(request):
    users = User.objects.all()
    form = UserForms()
    context = {'users':users}
    return render(request, "user_view.html", context)

def user_detail(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Account Deleted successfully')
        return redirect(reverse("users_view"))
    context= {
        'user':user,
        
    }
    return render(request, "user_details.html", context)


def user_update(request,id):
    user = User.objects.get(id= id)
    
    if request.method == 'POST':
        form = UserForms(request.POST,instance=user)
        if form.is_valid():
            form.save() 
            return redirect(reverse("details",args=[user.id]))
    else:
        form = UserForms(instance=user)
    context = {
        'form' : form
    }
    return render(request, "user_update.html", context)


def create_user(request):
    if request.method == "POST":  
        form = UserCreate(request.POST)  
        if form.is_valid():  
            form.save()  
            
            messages.success(request, 'Account created successfully')

            return redirect(reverse("users_view"))
  
    else:  
        form = UserCreate()  
    context = {
        'form':form
    }

    return render(request, "user_add.html", context)