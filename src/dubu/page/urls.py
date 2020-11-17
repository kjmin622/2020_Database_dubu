from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    #main
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('rooms',views.rooms,name="rooms"),
    path('login',views.adminLogin,name="login"),
    path('signup',views.adminLogout,name="signup"),

    #admin
    path('admin',admin_views.admin,name="admin"),
    path('admin/login',admin_views.adminLogin,name="admin_login"),
    path('admin/logout',admin_views.adminLogout,name="admin_logout"),
    path('admin/manage_depart',admin_views.manage_depart,name="manage_depart"),

]