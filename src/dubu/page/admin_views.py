from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import connection
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import *

def admin(request):
    if("staff_id" not in request.session or request.session["staff_id"] is None):
        return adminLogin(request)
    return render(request,'admin/admin_index.html',{})

def adminLogin(request):
    if("staff_id" in request.session and request.session["staff_id"] is not None):
        return admin(request)
    if(request.method == "POST"):
        staffId = request.POST["staff_id"]
        cursor = connection.cursor()
        strSql = "select * from page_staff where staff_id="+staffId
        result = cursor.execute(strSql)
        books = cursor.fetchall()
        connection.close()
        if(books):
            request.session["staff_id"]=staffId
            return admin(request)
        else:
            return render(request,'admin/admin_login.html')
    else:
        return render(request,'admin/admin_login.html')

def adminLogout(request):
    request.session["staff_id"] = None
    return admin(request)


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

    return render(request,'admin/manage_depart.html',{'datas':datas})