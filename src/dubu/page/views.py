from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.db import connection
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request,'main/index.html',{})

def about(request):
    return render(request,'main/about.html',{})

def rooms(request):
    return render(request,'main/rooms-single.html',{})

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