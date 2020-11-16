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