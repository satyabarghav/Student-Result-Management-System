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
    path("coursesform/",views.coursesForm,name="coursesForm"),
    path("getRegCourses/",views.getCourses,name="getCourses"),
    path('award_marks/', views.award_marks, name='award_marks'),
    path('add_student/', views.add_student, name='add_student'),
    path('update_student/<int:student_id>/', views.update_student, name='update_student'),
]