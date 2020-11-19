from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import connection
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
# Create your views here.

def index(request):
    return render(request,'main/index.html',{})

def about(request):
    return render(request,'main/about.html',{})

def rooms(request):
    return render(request,'main/rooms-single.html',{})

def login(request):
    if request.method == "POST":
        member_id = request.POST['member_id'];password = request.POST['password']
    try:
        #조건 미충족
        if request.POST["member_id"] == '' or request.POST["password"] == '':
            return render(request,'main/tlogin.html',{'Error': 'Fill all the blanks.'})
        cursor = connection.cursor()
        sqlStr = f"select member_id, password from page_member_info where member_id = '{member_id}' and password = '{password}'"
        result = cursor.execute(sqlStr)
        is_member=cursor.fetchall()
        if(is_member):
            request.session["member_id"]=member_id
            return redirect('index')    
        else:
            return render(request, 'main/tlogin.html', {'Error': 'Member ID or PW is incorrect'})
    except:
        connection.rollback()
        connection.close()
        return render(request,'main/tlogin.html',{})

def mypage(request):
    return render(request,'main/mypage.html',{})

def logout(request):
    request.session["member_id"]=None
    return render(request,'main/index.html',{})

def signup(request):
    if(request.method=="POST"):
        #last_name, first_name, birth, phone, email, member_id, password, password2, is_sms
        print(request.POST)
        last_name = request.POST["last_name"];first_name = request.POST["first_name"];birth = request.POST["birth"];phone = request.POST["phone"];email = request.POST["email"];member_id = request.POST["member_id"];password = request.POST["password1"];password2 = request.POST["password2"];is_sms = request.POST["is_sms"]
        
        try:
            #조건 미충족
            if (request.POST["last_name"] == '' or request.POST["first_name"] == '' or request.POST["birth"] == '' or request.POST["phone"] == '' or request.POST["email"] == '' or request.POST["member_id"] == '' or request.POST["password1"] == '' or request.POST["password2"] == ''):
                return render(request,'main/tsignup.html',{'Error': 'Fill all the blanks.'})
            if(password!=password2): 
                return render(request,'main/tsignup.html',{'Error': 'Password is not correctly checked.'})
            cursor = connection.cursor()
            sqlStr = f"select member_id from page_member_info where member_id = '{member_id}'"
            result = cursor.execute(sqlStr)
            is_member_id=cursor.fetchall()
            if(is_member_id):
                return render(request,'main/tsignup.html',{'Error': 'This ID is already in use.'})
            sqlStr = f"insert into page_member_info(last_name, first_name, birth, phone, email, member_id, password, is_sms, membership) values('{last_name}','{first_name}','{birth}','{phone}','{email}','{member_id}','{password}','{1 if is_sms=='on' else 0}',0)"
            result = cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return redirect('login')
        
        except:
            connection.rollback()
            connection.close()
            return render(request,'main/tsignup.html',{'Error': sqlStr})
    else:
        return render(request,'main/tsignup.html',{"Error":"회원가입"})
       
# admin
def staff(request):
    return render(request,'admin/staff.html',{})

def logout(request):
    request.session["member_id"]=None
    return render(request,'main/index.html',{})

def signup(request):
    if(request.method=="POST"):
        #last_name, first_name, birth, phone, email, member_id, password, password2, is_sms
        print(request.POST)
        last_name = request.POST["last_name"];first_name = request.POST["first_name"];birth = request.POST["birth"];phone = request.POST["phone"];email = request.POST["email"];member_id = request.POST["member_id"];password = request.POST["password1"];password2 = request.POST["password2"];is_sms = request.POST["is_sms"]
        
        try:
            #조건 미충족
            if (request.POST["last_name"] == '' or request.POST["first_name"] == '' or request.POST["birth"] == '' or request.POST["phone"] == '' or request.POST["email"] == '' or request.POST["member_id"] == '' or request.POST["password1"] == '' or request.POST["password2"] == ''):
                return render(request,'main/tsignup.html',{'Error': 'Fill all the blanks.'})
            if(password!=password2): 
                return render(request,'main/tsignup.html',{'Error': 'Password is not correctly checked.'})
            cursor = connection.cursor()
            sqlStr = f"select member_id from page_member_info where member_id = '{member_id}'"
            result = cursor.execute(sqlStr)
            is_member_id=cursor.fetchall()
            if(is_member_id):
                return render(request,'main/tsignup.html',{'Error': 'This ID is already in use.'})
            sqlStr = f"insert into page_member_info(last_name, first_name, birth, phone, email, member_id, password, is_sms, membership) values('{last_name}','{first_name}','{birth}','{phone}','{email}','{member_id}','{password}','{1 if is_sms=='on' else 0}',0)"
            result = cursor.execute(sqlStr);cursor.fetchall()
            connection.commit()
            connection.close()
            return redirect('login')
        
        except:
            connection.rollback()
            connection.close()
            return render(request,'main/tsignup.html',{'Error': sqlStr})
    else:
        return render(request,'main/tsignup.html',{"Error":"회원가입"})

        
        
        
        
