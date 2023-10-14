from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("facultyhome/",views.facultyHome,name = "facultyHome"),
    path("faculty_logout/",views.facultyLogout,name="faculty_logout"),
]