from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('rooms',views.rooms,name="rooms"),
    path('admin',admin_views.admin,name="admin"),
    path('admin/login',admin_views.adminSignin,name="admin_login"),
]