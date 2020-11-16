from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    #main
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('rooms',views.rooms,name="rooms"),

    #admin
    path('admin',admin_views.admin,name="admin"),
    path('admin/login',admin_views.adminLogin,name="admin_login"),
    path('admin/logout',admin_views.adminLogout,name="admin_logout"),
    path('admin/manage_depart',admin_views.manage_depart,name="manage_depart"),
    path('admin/manage_staff',admin_views.manage_staff,name="manage_staff"),

    #tool
    path('admin/manage_staff/del',admin_views.delete_staff,name="delete_staff"),
    path('admin/manage_staff/add',admin_views.insert_staff,name="insert_staff"),
    path('admin/manage_staff/edit',admin_views.edit_staff,name="edit_staff"),

]