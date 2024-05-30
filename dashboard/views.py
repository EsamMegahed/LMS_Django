from django.shortcuts import redirect, render
from django.urls import reverse
from .models import UserView
from django.contrib.auth.models import User
from .forms import UserForms
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