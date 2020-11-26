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

def example_view1(request):
    return render(request,"example/example1.html",{'request':request.POST})

def example_view2(request):
    if(request.method=="POST"):
        return render(request,"example/example2.html",{'request':request.POST})

    #POST로 넘어온게 아니면 처음 화면으로
    return redirect('example_url1')


#모든 값을 받아왔을 때의 views
def example_insert_db(request):
    if(request.method=="POST"):
        date1=request.POST["date1"]
        date2=request.POST["date2"]
        input1=request.POST["input1"]
        input2=request.POST["input2"]
        input3=request.POST["input3"]
        print(date1,date2,input1,input2,input3)
        #요로코롬 받아온 값들을 가지고 적절히 디비에 넣자!
        #...
        #예약이 완료됐을 시 이동해야 할 페이지로 적절히 리다이렉트해주자. 여기 예제에선 index로 이동
        return redirect('index')

    #POST로 넘어온게 아니면 처음 화면으로
    return redirect('example_url1')

