from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import connection
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import resolve_url
from django.shortcuts import redirect
from .models import *
from .tools import *

def adminLogin(request):
    if("staff_id" in request.session and request.session["staff_id"] is not None):
        return redirect('staff')
    if(request.method == "POST"):
        staffId = request.POST["staff_id"]
        cursor = connection.cursor()
        strSql = "select * from page_staff where staff_id='"+staffId+"'"
        result = cursor.execute(strSql)
        books = cursor.fetchall()
        connection.close()
        if(books):
            request.session["staff_id"]=staffId
            return redirect('staff')
        else:
            request.POST={}
            return render(request,'admin/admin_login.html')
    else:
        return render(request,'admin/admin_login.html')

def adminLogout(request):
    request.session["staff_id"] = None
    return redirect('admin_login')


# admin
def staff(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    try:
        staff_id = request.session["staff_id"]
        staff_datas = Staff.get_staff(staff_id)
        staff_working = Staff.staff_working_day(staff_id)
        if(staff_datas == None): 
            return redirect('admin_logout')
        return render(request,'admin/staff.html',{'datas':staff_datas,'working_datas':staff_working})

    except:
        connection.close()
        return redirect('admin_logout')

def s_reservation(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    return render(request,'admin/s_reservation.html',{})

def room_select(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')

    return render(request,'admin/room_select.html',{})

def parking(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    return render(request,'admin/parking.html',{})

def product(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    return render(request,'admin/product.html',{})

def engineer(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    return render(request,'admin/engineer.html',{})

def bill(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    return render(request,'admin/bill.html',{})

def staff_search(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    datas = Staff.get_staff()
    working_datas = Staff.get_staff_working()
    holiday_datas = Staff.get_staff_holiday()
    return render(request,'admin/staff_search.html',{'datas':datas, 'working_datas':working_datas, 'holiday_datas':holiday_datas})

def management(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    datas = Staff.get_staff()
    working_datas = Staff.get_staff_working()
    holiday_datas = Staff.get_staff_holiday()
    names = ['staff_id', 'rank', 'status', 'depart_id', 'team', 'first_name', 'last_name', 'phone', 'bank', 'account', 'wide_area_unit', 'street', 'basic_unit', 'si_gu', 'eub_myeon', 'building_number', 'detail_address']
    return render(request,'admin/management.html',{'datas':datas, 'working_datas':working_datas, 'holiday_datas':holiday_datas, 'names':names})



def manage_depart(request):
    if(request.method == "POST"):
        try:
            depart_id = request.POST.get("depart_id")+','
            depart_name = request.POST.get("depart_name")+','
            position = request.POST.get("position")
            
            cursor = connection.cursor()
            sqlStr = "insert into page_depart values("+depart_id+depart_name+position+")"
            result = cursor.execute(sqlStr)
            cursor.fetchall()
            connection.commit()
            connection.close()
        except:
            connection.rollback()
            connection.close()
    
    cursor = connection.cursor()
    sqlStr = "select * from page_depart"
    result = cursor.execute(sqlStr)
    dataSet = cursor.fetchall()
    connection.close()
    datas = []
    for data in dataSet:
        datas.append(str(data).replace("'",'').replace('(','').replace(')','').replace(',',' /'))

    return render(request,'develop/manage_depart.html',{'datas':datas})


@csrf_exempt
def delete_staff(request):
    if(request.method=="POST"):
        Staff.delete_staff(request.POST)
    
    return redirect('manage_staff')

@csrf_exempt
def insert_staff(request):
    if(request.method=="POST"):
        Staff.insert_staff(request.POST)
    
    return redirect('manage_staff')

@csrf_exempt
def edit_staff(request):
    if(request.method=="POST"):
        Staff.edit_staff(request.POST)
    return redirect('manage_staff')

@csrf_exempt
def insert_staff_working(request):
    if(request.method=="POST"):
        Staff.insert_staff_working(request.POST)
    return redirect('manage_staff')

@csrf_exempt
def insert_staff_holiday(request):
    if(request.method=="POST"):
        Staff.insert_staff_holiday(request.POST)
    return redirect('manage_staff')

@csrf_exempt
def delete_staff_working(request):
    if(request.method=="POST"):
        Staff.delete_staff_working(request.POST)
    return redirect('manage_staff')

@csrf_exempt
def delete_staff_holiday(request):
    if(request.method=="POST"):
        Staff.delete_staff_holiday(request.POST)
    return redirect('manage_staff')

@csrf_exempt
def change_staff_status(request):
    if(request.method=="POST"):
        Staff.change_staff_status(request.POST)
    return redirect('staff')


@csrf_exempt
def insert_room_type(request):
    if(request.method=="POST"):
        print(request.POST)

    return redirect('manage_room')

