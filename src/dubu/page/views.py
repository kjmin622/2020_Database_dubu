from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import connection
from django.shortcuts import redirect
from django.contrib import messages
from django.template import loader
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from datetime import datetime
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
        redirect('login')
    # login
    else:
       login = True
    # #reserve
    return render(request,'main/reservation.html',{})

def reservation2(request):
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None :
        login = False
    # login
    else:
        login = True
    
    if(request.method=='POST'):
        if(request.POST['method']=='reservation'):
            # check_in = request.POST['check_in'];check_out = request.POST['check_out'];adult_num = int(request.POST['adult_num']);child_num= int(request.POST['child_num'])
            # if(request.POST['check_in']=='' or request.POST['check_out']=='' or check_in>=check_out or datetime.today().strftime("%Y-%m-%d")>=check_in):
            #     return redirect('reservation')
            # if(adult_num<=0 or (adult_num+child_num)==0 or (adult_num+child_num)>=4):
            #     return redirect('reservation')
            return render(request,'main/reservation2.html',{'request':request.POST})
    return redirect('reservation')

def reservation3(request):
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None :
        login = False
    # login
    else:
        login = True
    return render(request,'main/reservation3.html',{"login":login})    

def join(request):
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None :
        return render(request,'main/join.html',{})  
    # login
    else :
        return render(request,'main/mypage.html',{})

def mypage(request):
    return render(request,'main/mypage.html',{})

def signup(request):
    if(request.method=="POST"):
        #last_name, first_name, birth, phone, email, member_id, password, password2, is_sms
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


def login(request):
     # not login
    if('member_id' in request.session and request.session["member_id"]!=None):
        return redirect('index')
    
    if request.method == "POST":
        try: # 로그인
            #조건 미충족
            print(request.POST)
            member_id = request.POST['member_id']; password = request.POST['password']
            cursor = connection.cursor()
            sqlStr = f"select member_id from page_member_info where member_id = '{member_id}' and password = '{password}'"
            result = cursor.execute(sqlStr)
            is_member=cursor.fetchall()
            connection.close()
            if(is_member):
                request.session["member_id"]=member_id
                return redirect('index')
            else:
                return redirect('login')
        except:
            connection.rollback()
            connection.close()
            return redirect('login')

    member_datas = []
    try:
        cursor = connection.cursor()
        sqlStr = "select member_id, last_name, first_name, phone, email, password from page_member_info"
        cursor.execute(sqlStr)
        result=cursor.fetchall()
        for data in result:
            member_datas.append({'member_id':data[0], 'last_name':data[1], 'first_name':data[2], 'phone':data[3], 'email':data[4], 'password':data[5]})
        connection.close()
    except:
        connection.close()
    return render(request, 'main/login.html',{'member_datas':member_datas})


def logout(request):
    request.session["member_id"]=None
    return redirect('index')
       
# admin
def staff(request):
    return render(request,'admin/staff.html',{})

def room_select(request):
    return render(request,'admin/room_select.html',{})

def parking(request):
    return render(request,'admin/parking.html',{})

def product(request):
    return render(request,'admin/product.html',{})