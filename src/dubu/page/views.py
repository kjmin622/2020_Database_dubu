from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import connection
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

def index(request):
    return render(request,'main/index.html',{})

def about(request):
    return render(request,'main/about.html',{})

def rooms(request):
    return render(request,'main/rooms-single.html',{})

<<<<<<< HEAD
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
        if (request.POST["last_name"] == '' or
           request.POST["first_name"] == '' or
           request.POST["birth"] == '' or
           request.POST["phone"] == '' or
           request.POST["email"] == '' or
           request.POST["member_id"] == '' or
           request.POST["password1"] == '' or
           request.POST["password2"] == ''):
            return render(request,'main/signup.html',{'Error': 'Fill all the blanks.'})

        if request.POST["password1"] == request.POST["password2"]:
            member_info = User.objects.create_member_info(
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

def signup(request):
    if(request.method=="POST"):
        #last_name, first_name, birth, phone, email, member_id, password, password2, is_sms
        last_name = request.POST["last_name"];first_name = request.POST["first_name"];birth = request.POST["birth"];phone = request.POST["phone"];email = request.POST["email"];member_id = request.POST["member_id"];password = request.POST["password1"];password2 = request.POST["password2"];is_sms = request.POST["is_sms"])
        
        try:
            #조건 미충족
            if (request.POST["last_name"] == '' or request.POST["first_name"] == '' or request.POST["birth"] == '' or request.POST["phone"] == '' or request.POST["email"] == '' or request.POST["member_id"] == '' or request.POST["password1"] == '' or request.POST["password2"] == ''):
                return render(request,'main/signup.html',{'Error': 'Fill all the blanks.'})
            if(password!=password2): 
                return render(request,'main/signup.html',{'Error': 'Password is not correctly checked.'})
    
            cursor = connection.cursor()
            sqlStr = f"select member_id from page_member_info where member_id = {member_id}"
            result = cursor.execute();member_id=cursor.fetchall()
            if(member_id):
                return render(request,'main/signup.html',{'Error': 'This ID is occupied.'})

            sqlStr = f"insert into page_member_info(member_id,membership,birth,is_sms,)"

        
        
        
        
=======
def reservation(request):
    return render(request,'main/reservation.html',{})

def join(request):
    return render(request,'main/join.html',{})

def event(request):
    return render(request,'main/event.html',{})

def login(request):
    return render(request,'main/login.html',{})

def mypage(request):
    return render(request,'main/mypage.html',{})

# admin
def staff(request):
    return render(request,'admin/staff.html',{})

def s_reservation(request):
    return render(request,'admin/s_reservation.html',{})

def room_select(request):
    return render(request,'admin/room_select.html',{})

def parking(request):
    return render(request,'admin/parking.html',{})

def product(request):
    return render(request,'admin/product.html',{})

def engineer(request):
    return render(request,'admin/engineer.html',{})

def staff_search(request):
    return render(request,'admin/staff_search.html',{})
>>>>>>> develop
