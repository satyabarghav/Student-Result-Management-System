from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Student
from django.db.models import Sum


from .models import Admin, Student, Faculty, Course


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
def getCourses(request):
    id = request.POST.get("id_number")
    student = Student.objects.get(studentId=id)
    enrolled_courses = student.courses.all()
    return render(request,"viewCourses.html",{"coursesData":enrolled_courses})

def coursesForm(request):
    return render(request,"getCourses.html")

from django.shortcuts import render, redirect
from .forms import MarksForm, StudentForm


def award_marks(request):
    if request.method == 'POST':
        form = MarksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page or a different view
    else:
        form = MarksForm()

    return render(request, 'award_marks.html', {'form': form})


class StudentUpdateForm:
    pass


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewstudents')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


def update_student(request, student_id):
    student = get_object_or_404(Student, studentId=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('viewstudent')
    else:
        form = StudentForm(instance=student)

    return render(request, 'update_student.html', {'form': form, 'student': student})
