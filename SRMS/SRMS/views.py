from django.http import HttpResponse
from django.shortcuts import render



def demofunction(request):
    return HttpResponse("Welcome to PFSD SDP Project Home")


def home(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def contact(request):
    return render(request,"contact.html")


def login(request):
    return render(request,"login.html")