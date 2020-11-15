from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('admin',views.admin,name="admin"),
    path('admin/login',views.adminSignin,name="admin_login"),
]