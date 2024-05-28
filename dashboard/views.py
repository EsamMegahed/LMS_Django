from django.shortcuts import render

# Create your views here.

def dash(request):
    context= {}
    return render(request, "dashboard_base.html", context)
