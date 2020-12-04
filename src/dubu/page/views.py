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
from datetime import date
import time
import datetime
from .tools import *
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

def get_member(member_id=""):
        try:
            cursor = connection.cursor()
            #sqlStr = "select staff_id, first_name, last_name, rank,depart_id, status,bank,account, phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon, building_number, detail_address, team_name from page_staff  natural join (select * from page_team_staff natural join (select page_staff_info.staff_id, first_name, last_name, bank,account,phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon,building_number,detail_address from page_staff_address inner join page_staff_info on page_staff_info.staff_id = page_staff_address.staff_id))"
            sqlStr="select member_id, membership, birth, is_sms, password, email, first_name, last_name, phone, point from page_member_info"
            result=cursor.execute(sqlStr)
            datas=cursor.fetchall()
            output_data=[]
            for data in datas:
                output_data.append({'member_id':data[0], 'membership':data[1], 'birth':data[2], 'is_sms':data[3],
                                    'password':data[4], 'email':data[5], 'first_name':data[6], 'last_name':data[7],
                                    'phone':data[8],'point':data[9]})
            if(member_id!=""):
                for data in output_data:
                    if(data["member_id"]==member_id):
                        return data
                raise ValueError
            return output_data
        except:
            connection.rollback()
            connection.close()
        return None

def get_room(room_type=""):
    try:
        cursor = connection.cursor()
        #sqlStr = "select staff_id, first_name, last_name, rank,depart_id, status,bank,account, phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon, building_number, detail_address, team_name from page_staff  natural join (select * from page_team_staff natural join (select page_staff_info.staff_id, first_name, last_name, bank,account,phone,wide_area_unit,basic_unit,street,si_gu,eub_myeon,building_number,detail_address from page_staff_address inner join page_staff_info on page_staff_info.staff_id = page_staff_address.staff_id))"
        sqlStr = "select room_type, price, mem_limit, photo_url, bed_type, bed_num from page_room_type natural join page_room_type_bed"
        result = cursor.execute(sqlStr)
        datas = cursor.fetchall()
        output_data = []
        for data in datas:
            output_data.append({'room_type':data[0], 'price':data[1], 'mem_limit':data[2], 'photo_url':data[3], 'bed_type':data[4], 'bed_num':data[5]})

        sqlStr = "select count(room_num), room_type from (select room_num, room_type from page_rooms where room_num not in (select room_num from page_booking_rooms)) group by room_type"
        cursor.execute(sqlStr);result=cursor.fetchall()
        output2 = []
        for data in result:
            output2.append({"room_num":data[0],"room_type":data[1]})
            
        return output_data, output2
    except:
        connection.rollback()
        connection.close()
    return None

def reservation(request):
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None :
        login = False
        return redirect('login')
    # login
    else:
       login = True
    # #reserve
    return render(request,'main/reservation.html',{"login":login})

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
            room_datas, room_info = get_room()
            repost = dict(request.POST)
            tmp = ["check_in","check_out","adult_num","child_num"]
            for t in tmp:
                repost[t] = repost[t][0]
            repost["total_num"] = int(repost["adult_num"])+int(repost["child_num"])
            return render(request,'main/reservation2.html',{'request':repost, 'room_datas': room_datas, 'room_info':room_info, 'login':login})

    return redirect('reservation')

def reservation3(request):
    # not login
    if "member_id" not in request.session or request.session["member_id"]==None :
        login = False
    # login
    else:
        login = True

    if(request.method=='POST'):
        if(request.POST['method']=='reservation2'):
            # check_in = request.POST['check_in'];check_out = request.POST['check_out'];adult_num = int(request.POST['adult_num']);child_num= int(request.POST['child_num'])
            # if(request.POST['check_in']=='' or request.POST['check_out']=='' or check_in>=check_out or datetime.today().strftime("%Y-%m-%d")>=check_in):
            #     return redirect('reservation')
            # if(adult_num<=0 or (adult_num+child_num)==0 or (adult_num+child_num)>=4):
            #     return redirect('reservation')

            member_id = request.session["member_id"]
            member_datas = get_member(member_id)
            return render(request,'main/reservation3.html',{'request':request.POST, 'login': login, 'member_datas':member_datas})
        else:
            member_id = request.session["member_id"]
            print(Book.insert_book(request.POST, member_id))
            return redirect('login')
    return redirect('reservation2')      

def mypage(request):
    if("member_id" not in request.session or request.session["member_id"]==None): return redirect('login')
    if(request.method=="POST"):
        if(request.POST['method']=='delete'):
            Book.delete_booking(request.POST)

        elif(request.POST['password']!='' and request.POST['phone']!='' and request.POST['email']!=''):
            cursor = connection.cursor()
            member_id = request.session["member_id"]
            sqlStr = f"update page_member_info set password='{request.POST['password']}', phone='{request.POST['phone']}', email='{request.POST['email']}' where member_id='{member_id}'"
            print(sqlStr)
            cursor.execute(sqlStr)
            cursor.fetchall()
            connection.commit()
            connection.close()
            return redirect('mypage')
    try:
        member_id = request.session["member_id"]
        member_datas = get_member(member_id)
        if(member_datas == None): 
            return redirect('logout')
        booking_datas=Book.get_booking_info(member_id)
        coupon_datas=Book.get_coupon()
        return render(request,'main/mypage.html',{'member_datas':member_datas, 'booking_datas':booking_datas, 'coupon_datas':coupon_datas})
    except:
        connection.close()
        return redirect('logout')

def join(request):
    if(request.method=="POST"):
        print(1)
        #last_name, first_name, birth, phone, email, member_id, password, password2, is_sms
        last_name = request.POST["last_name"];first_name = request.POST["first_name"];phone=request.POST['phone_1']+request.POST['phone_2']+request.POST['phone_3'];birth = request.POST['birth_year']+'-'+request.POST['birth_month']+'-'+request.POST['birth_day'];email = request.POST["email"];member_id = request.POST["member_id"];password = request.POST["password"];password2 = request.POST["password2"];is_sms = request.POST["is_sms"]
        try:
            #조건 미충족
            if (request.POST["last_name"] == '' or request.POST["first_name"] == '' or request.POST['phone_1']+request.POST['phone_2']+request.POST['phone_3'] == '' or request.POST['birth_year']+'-'+request.POST['birth_month']+'-'+request.POST['birth_day'] == '' or  request.POST["email"] == '' or request.POST["member_id"] == '' or request.POST["password"] == '' or request.POST["password2"] == ''):
                return redirect('join')
 
            cursor = connection.cursor()
            sqlStr = f"insert into page_member_info(last_name, first_name, birth, phone, email, member_id, password, is_sms, membership, point) values('{last_name}','{first_name}','{birth}','{phone}','{email}','{member_id}','{password}','{1 if is_sms=='on' else 0}','classic',0)"
            sqlStr2= f"update page_member_info set point=point+5000 where member_id='{request.POST['referrer']}'"
            cursor.execute(sqlStr)
            cursor.fetchall()
            cursor.execute(sqlStr2)
            cursor.fetchall()
            connection.commit()
            connection.close()
            return redirect('login')
        except:
            connection.rollback()
            connection.close()
            return redirect('join')
    else:
        member_datas = get_member()
        if(member_datas == None): 
            return redirect('join')
        return render(request,'main/join.html',{'member_datas':member_datas})


def login(request): #status=logout
     # logout
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