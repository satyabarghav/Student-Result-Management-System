from django.shortcuts import render

def facultyHome(request):
    return render(request,"facultyHome.html")
def facultyLogout(request):
    return render(request,"login.html")
