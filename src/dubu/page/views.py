from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages
from django.template import loader
from .models import *
from .forms import *
# Create your views here.

def index(request):  
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None :
        login = False
    # login
    else:
        login = True
    return render(request,'main/index.html',{"login":login})

def about(request):
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None :
        login = False
    # login
    else:
        login = True
    return render(request,'main/about.html',{"login":login})

def rooms(request):
    return render(request,'main/rooms-single.html',{})

def reservation(request):
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None :
        login = False
    # login
    else:
        login = True
    return render(request,'main/reservation.html',{"login":login})

def join(request):
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None :
        return render(request,'main/join.html',{})  
    # login
    else :
        return render(request,'main/mypage.html',{})

def event(request):
    return render(request,'main/event.html',{})

def login(request):
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None : 
        if request.method == "POST":
            #login start
            if(request.POST["input"]=="login"):
                member_id = request.POST['member_id']; password = request.POST['password']
                try:
                    #조건 미충족
                    if request.POST["member_id"] == '' or request.POST["password"] == '':
                        return render(request,'main/login.html',{'Error': 'Fill all the blanks.'})
                    cursor = connection.cursor()
                    sqlStr = f"select member_id, password from page_member_info where member_id = '{member_id}' and password = '{password}'"
                    result = cursor.execute(sqlStr)
                    is_member=cursor.fetchall()
                    if(is_member):
                        request.session["member_id"]=member_id
                        return redirect('index')
                    else:
                        return render(request, 'main/login.html', {'Error': 'Member ID or PW is incorrect'})
                except:
                    connection.rollback()
                    connection.close()
                    return render(request,'main/login.html',{})
            #id
            elif request.POST["input"]=="find_id":
                try:
                    member_id = request.POST['member_id']; last_name = request.POST['last_named']; first_name = request.POST['first_name']; email = request.POST['email']
                    info = False
                    cursor = connection.cursor()
                    sqlStr = f"select member_id from page_member_info where last_name = '{last_name}' and first_name = '{first_name}' and email = '{email}'"
                    result = cursor.execute(sqlStr)
                    is_member=cursor.fetchall()
                    if(is_member): 
                        info = True
                        member_id = is_member
                        return render(request, 'main/login.html', {})
                    else:
                        return render(request, 'main/index.html', {'Error': 'Your information is incorrect'})
                except:
                    connection.rollback()
                    connection.close()
                    return render(request,'main/login.html',{})
            #pw
            elif request.POST["input"]=="find_pw":
                try:
                    member_id = request.POST['member_id'];last_name = request.POST['last_name'];first_name = request.POST['first_name'];email = request.POST['email']
                    cursor = connection.cursor()
                    sqlStr = f"select password from page_member_info where last_name = '{last_name}' and first_name = '{first_name}' and member_id = '{member_id}' and email = '{email}'"
                    result = cursor.execute(sqlStr)
                    is_member=cursor.fetchall()
                    print(is_member)
                    if(is_member): 
                        password = str(is_member[0][0])
                        return render(request, 'main/login.html',{'info':'find_password','password':password})
                    else:
                        return render(request, 'main/index.html', {'Error': 'Your information is incorrect'})
                except:
                    connection.rollback()
                    connection.close()
                    return render(request,'main/about.html',{})
            else:
                return redirect('login')

        else:
            return render(request, 'main/login.html')
        return redirect('login')

    # already login
    else : 
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
        return render(request,'main/tsignup.html',{"Error":""})

def mypage(request):

    return render(request,'main/mypage.html',{})

# admin
def staff(request):
    return render(request,'admin/staff.html',{})

# def s_reservation(request):
#     return render(request,'admin/s_reservation.html',{})

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