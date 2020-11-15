from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import connection
from .models import *
from .forms import *

def admin(request):
    return HttpResponse("Hello, this is adminPage")

def adminSignin(request):
    if(request.method == "POST"):
        form = adminLoginForm(request.POST)
        sfid = request.POST['staff_id']
        cursor = connection.cursor()
        sql = "SELECT staff_id FROM page_staff WHERE staff_id=="+sfid
        result = cursor.execute(sql)
        print(result)

        if(user is not None):
            login(request,user)
            return redirect('admin')
        else:
            return HttpResponse('fail')
    else:
        form = adminLoginForm()
        return render(request,'admin/admin_login.html')
