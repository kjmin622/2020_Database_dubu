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
            return redirect('admin_login')
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

def room_select(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    if(request.method=="POST"):
        Book.select_room(request.POST)
    booking_datas = Book.get_booking_info()
    room_datas = Book.get_room_list()
    return render(request,'admin/room_select.html',{"booking_datas":booking_datas,'room_datas':room_datas})


@csrf_exempt
def parking(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    if(request.method=="POST"):
        try:
            if(request.POST["method"]=="out_car"):
                Book.delete_parking(request.POST)
            elif(request.POST["method"]=="in_car"):
                Book.insert_parking(request.POST)
            return redirect('parking')
        except:
            return redirect('parking')
    parking_datas = Book.get_parking_info()
    return render(request,'admin/parking.html',{'parking_datas':parking_datas})

def product(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    if(request.method=="POST"):
        #product_edit
        if(request.POST["method"]=="product_edit"):
            Product.edit_product(request.POST)
            return redirect('product')

        #add_purchase
        if(request.POST["method"]=="add_purchase"):
            rp = dict(request.POST)
            rp["staff_id"]=request.session["staff_id"]
            Product.insert_purchase(rp)
            return redirect('product')

        #complete_purchase
        if(request.POST["method"]=="purchase_complete"):
            Product.complete_purchase(request.POST)
            return redirect('product')
    product_datas = Product.get_product()
    purchase_datas = Product.get_purchase()
    return render(request,'admin/product.html',{'product_datas':product_datas,'purchase_datas':purchase_datas})


def bill(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    if(request.method=="POST"):
        if("method" in request.POST and request.POST["method"]=="insert_purchase"):
            Book.insert_purchase(request.POST)
        if("method" in request.POST and request.POST["method"]=="offer_complete"):
            Book.offer_complete(request.POST)
        else:
            Book.complete_bill(request.POST)


    invoice_datas = Book.get_invoice()
    coupon_datas = Book.get_coupon()
    point_datas = Book.get_point()
    return render(request,'admin/bill.html',{'invoice_datas':invoice_datas,'coupon_datas':coupon_datas, 'point_datas':point_datas})

def staff_search(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    datas = Staff.get_staff()
    working_datas = Staff.get_staff_working()
    holiday_datas = Staff.get_staff_holiday()
    return render(request,'admin/staff_search.html',{'datas':datas, 'working_datas':working_datas, 'holiday_datas':holiday_datas})


# <th>booking_id</th><th>name</th><th>phone</th><th>is_check_in</th><th>check_in</th><th>check_out</th><th>room_num</th><th>room_type</th><th>adult_num</th><th>child_num</th><th>baby_num</th><th>breakfast</th><th>extra_text</th>
def management(request):
    if(not Staff.staff_login_check(request)): return redirect('admin_login')
    datas = Staff.get_staff()
    working_datas = Staff.get_staff_working()
    holiday_datas = Staff.get_staff_holiday()
    names = ['staff_id', 'rank', 'status', 'depart_id', 'team', 'first_name', 'last_name', 'phone', 'bank', 'account', 'wide_area_unit', 'street', 'basic_unit', 'si_gu', 'eub_myeon', 'building_number', 'detail_address']
    booking_names = ['booking_id', 'first_name','last_name', 'phone', 'is_check_in', 'check_in', 'check_out', 'room_num', 'room_type', 'adult_num', 'child_num', 'baby_num', 'breakfast', 'extra_text']
    engineering_names = ['facility_id', 'facility_name', 'team_name', 'check_date', 'check_limit', 'status']
    rooms_datas,room_type_datas,room_type_bed_datas = Room.get_room_info()
    booking_datas = Book.get_booking_info()
    engineering_datas = OtherTool.get_engineering()
    return render(request,'admin/management.html',{'datas':datas, 'working_datas':working_datas, 'holiday_datas':holiday_datas, 'names':names,
                                                    'rooms_datas':rooms_datas,'room_type_datas':room_type_datas,'room_type_bed_datas':room_type_bed_datas,
                                                    'booking_datas':booking_datas, 'booking_names':booking_names,
                                                    'engineering_datas':engineering_datas, 'engineering_names':engineering_names})



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
    
    return redirect('management')

@csrf_exempt
def insert_staff(request):
    if(request.method=="POST"):
        Staff.insert_staff(request.POST)
    
    return redirect('management')

@csrf_exempt
def edit_staff(request):
    if(request.method=="POST"):
        Staff.edit_staff(request.POST)
    return redirect('management')

@csrf_exempt
def insert_staff_working(request):
    if(request.method=="POST"):
        Staff.insert_staff_working(request.POST)
    return redirect('management')

@csrf_exempt
def insert_staff_holiday(request):
    if(request.method=="POST"):
        Staff.insert_staff_holiday(request.POST)
    return redirect('management')

@csrf_exempt
def delete_staff_working(request):
    if(request.method=="POST"):
        Staff.delete_staff_working(request.POST)
    return redirect('management')

@csrf_exempt
def delete_staff_holiday(request):
    if(request.method=="POST"):
        Staff.delete_staff_holiday(request.POST)
    return redirect('management')

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

@csrf_exempt
def edit_room_type(request):
    if(request.method=="POST"):
        Room.edit_room_type(request.POST)
    
    return redirect('management')

@csrf_exempt
def delete_booking(request):
    if(request.method=="POST"):
        Book.delete_booking(request.POST)
    
    return redirect('management')


@csrf_exempt
def edit_booking(request):
    if(request.method=="POST"):
        Book.edit_booking(request.POST)
    return redirect('management')

@csrf_exempt
def insert_booking(request):
    if(request.method=="POST"):
        Book.insert_booking(request.POST)
    return redirect('management')


@csrf_exempt
def delete_engineering(request):
    if(request.method=="POST"):
        OtherTool.delete_engineering(request.POST)
    return redirect('management')

@csrf_exempt
def edit_engineering(request):
    if(request.method=="POST"):
        OtherTool.edit_engineering(request.POST)
    return redirect('management')

@csrf_exempt
def insert_engineering(request):
    if(request.method=="POST"):
        OtherTool.insert_engineering(request.POST)
    return redirect('management')