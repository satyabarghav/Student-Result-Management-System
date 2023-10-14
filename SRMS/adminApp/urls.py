from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("adminhome/",views.adminHome,name = "adminHome"),
    path("admin_logout/",views.adminLogout,name="admin_logout"),
    path("logincheck/", views.checklogin, name="logincheck"),
    path("viewfaculty/",views.viewfaculty,name="viewfaculty"),
    path("viewstudent/",views.viewstudents,name="viewstudent"),
    path("viewcourse/",views.viewcourses,name="viewcourse"),
    path('results/<int:student_id>/', views.student_results, name='student_results'),
]