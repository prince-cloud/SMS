from django.urls import path
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth import views
from . import views

app_name = 'management'

urlpatterns = [
    path('', views.portal, name='portal'),
    path('logout/', views.logoutview, name='logout'),
    path('adminsite/', views.adminsite, name='adminsite'),
    path('portal/', views.portal, name='portal'),
    path('add_staff/', views.AddStaff.as_view(), name='AddStaff'),
    path('add_student/', views.AddStudent.as_view(), name='AddStudent'),
    path('staffportal/studentlist/', views.studentlist, name='studentlist'),
    
]

