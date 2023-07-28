from django.shortcuts import render

# Create your views here.

def loginview(request, *args,**kwargs):
    return render(request, "login.html", {})


def signupview(request, *args,**kwargs):
    return render(request, "singup.html", {})


def signupview2(request, *args,**kwargs):
    return render(request, "signup2.html", {})