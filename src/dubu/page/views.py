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
