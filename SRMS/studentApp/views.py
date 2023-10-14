from django.shortcuts import render

# Create your views here.
def studentHome(request):
    return render(request,"studentHome.html")


def studentLogout(request):
    return render(request,"login.html")
from django.shortcuts import render


