from django.shortcuts import render

def registeruser(request):
    return render(request,"register.html")

def loginuser(request):
    return render(request,"login.html")