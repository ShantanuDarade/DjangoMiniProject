from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from .models import Contact

# Create your views here.
def index(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        regno = request.POST.get('regno', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        year = request.POST.get('year', '')
        branch = request.POST.get('branch', '')
        address = request.POST.get('address', '')
        if name and regno and email and phone and year and branch and address:
            contact = Contact(name=name,regno=regno,email=email,phone=phone,year=year,branch=branch,address=address)
            contact.save()
            return HttpResponse("Information is saved")
        else:
            return HttpResponse("Please enter all the details!")
    return render(request,'index.html')