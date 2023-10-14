from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from .models import Admin, Student, Faculty, Course, Result


# Create your views here.
def adminHome(request):
    return render(request,"adminHome.html")
def adminLogout(request):
    return render(request,"login.html")
def checklogin(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    adminflag = False
    student_flag = False
    faculty_flag = False
    if not username.isnumeric():
        adminflag = Admin.objects.filter(Q(username=username)&Q(password=password))
    else:
        student_flag = Student.objects.filter(Q(studentId=int(username))&Q(password=password))
        faculty_flag = Faculty.objects.filter(Q(facultyId=int(username))&Q(password=password))
    if adminflag:
        return render(request,"adminHome.html")
    elif student_flag:
        return render(request,"studentHome.html")
    elif faculty_flag:
        return render(request,"facultyHome.html")
    else:
        return render(request,"login.html")
def viewfaculty(request):
    facultys = Faculty.objects.all()
    return render(request,"viewFaculty.html",{"facultysData":facultys})
def viewcourses(request):
    courses = Course.objects.all()
    return render(request,"viewCourses.html",{"coursesData":courses})
def viewstudents(request):
    students = Student.objects.all()
    return render(request,"viewStudents.html",{"studentsData":students})


def student_results(request, student_id):
    student_results = Result.objects.filter(student__studentId=student_id)
    return render(request, 'results.html', {'student_results': student_results})


# Create your views here.
