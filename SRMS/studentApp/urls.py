from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("studenthome/",views.studentHome,name = "studentHome"),
    path("student_logout/",views.studentLogout,name="student_logout"),
]