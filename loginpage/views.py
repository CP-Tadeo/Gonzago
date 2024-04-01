from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

from .models import Stall

def page_not_found(request):
    return HttpResponse("This page has been removed")


def log_in(request):
    message = ""
    return render(request, 'loginpage/detail.html', {'message': message})
#    return HttpResponse('Hello World! This came from the index view')

def log_in_attempt(request):
    message = "Incorrect reference key or password"
    if request.method == "POST":   # IF LOGGING IN
        refKey = request.POST.get("refKey")
        try: # CHECK IF STALL WITH REF KEY EXISTS
            stall_Obj = Stall.objects.get(referenceKey=refKey)
        except Stall.DoesNotExist:
            stall_Obj = None
        
        if stall_Obj: # IF STALL EXISTS
            passWord = request.POST.get("passWord")

            if stall_Obj.passWord == passWord: # CHECK PASSWORD
                #LOG IN
                return redirect('vendorpage/',{'stall': stall_Obj})
            else:
                return render(request, 'loginpage/detail.html',  {'message': message})
        else:
            return render(request, 'loginpage/detail.html',  {'message': message})

    return render(request, 'loginpage/detail.html', {'message': message})

    return HttpResponse(refKey, passWord)

    context = {}
    return render(request, "loginpage/detail.html", context)