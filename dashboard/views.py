from django.shortcuts import redirect, render
from django.urls import reverse
from .models import UserView
from django.contrib.auth.models import User
from .forms import UserForms,UserCreate
from django.core.paginator import Paginator
from django.contrib import messages
from .filters import UsersFilter
# Create your views here.

def dash(request):
    users = User.objects.all()
    user_filter = UsersFilter(request.GET,queryset=users)
    users = user_filter.qs
    paginator = Paginator(users,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {'users':page_obj,
               'user_filter':user_filter}
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