from django.urls import path
from . import views
from . import admin_views

urlpatterns = [
    #main
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('rooms',views.rooms,name="rooms"),
    path('reservation',views.reservation,name="reservation"),
    path('join',views.join,name="join"),
    path('event',views.event,name="event"),
    path('login',views.login,name="login"),
    path('mypage',views.mypage,name="mypage"),
 

    #admin
    path('admin',admin_views.admin,name="admin"),
    path('admin/login',admin_views.adminLogin,name="admin_login"),
    path('admin/logout',admin_views.adminLogout,name="admin_logout"),
    path('admin/manage_depart',admin_views.manage_depart,name="manage_depart"),

    # front admin
    path('admin/staff',admin_views.staff,name="staff"),
    path('admin/s_reservation',admin_views.s_reservation,name="s_reservation"),
    path('admin/room_select',admin_views.room_select,name="room_select"),
    path('admin/parking',admin_views.parking,name="parking"),
    path('admin/product',admin_views.product,name="product"),
    path('admin/engineer',admin_views.engineer,name="engineer"),
    path('admin/staff_search',admin_views.staff_search,name="staff_search"),

]