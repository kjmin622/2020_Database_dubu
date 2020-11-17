from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import connection
from .models import *
from .forms import *
from django.contrib.auth.models import Member
from django.contrib import auth
# Create your views here.

def index(request):
    return render(request,'main/index.html',{})

def about(request):
    return render(request,'main/about.html',{})

def rooms(request):
    return render(request,'main/rooms-single.html',{})

def login(request):
    if request.method == "POST":
        member_id = request.POST['member_id']
        password = request.POST['password']
        member = auth.authenticate(request, member_id=member_id, password=password)
        if member is not None:
            auth.login(request, member)
            return redirect('main/index.html')
        else:
            return render(request, 'main/login.html', {'Error': 'Member ID or Password is incorrect'})
    else:
        return render(request,'main/login.html',{})

def logout(request):
    auth.logout(request)
    return render(request,'main/index.html',{})

def signup(request):
    if request.method == "POST":
        if request.POST["last_name"] == '' or
           request.POST["first_name"] == '' or
           request.POST["birth"] == '' or
           request.POST["phone"] == '' or
           request.POST["email"] == '' or
           request.POST["member_id"] == '' or
           request.POST["password1"] == '' or
           request.POST["password2"] == '':
        return render(request,'main/signup.html',{'Error': 'Fill all the blanks.'})

        if request.POST["password1"] == request.POST["password2"]:
            member_info = Member.objects.create_member_info(
                last_name = request.POST["last_name"],
                first_name = request.POST["first_name"],
                birth = request.POST["birth"],
                phone = request.POST["phone"],
                email = request.POST["email"],
                member_id = request.POST["member_id"],
                password = request.POST["password1"],
                is_sms = request.POST["is_sms"])
            auth.login(request, member)
            return redirect('main/index.html')
        return render(request,'main/signup.html',{'Error': 'Password is not correctly checked.'})
    return render(request,'main/signup.html',)
