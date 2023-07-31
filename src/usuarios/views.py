from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 


# Create your views here.
def login(request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST['nome']
        password = request.POST['password']  
    return render(request, "usuarios/login.html", {})


def signup(request, *args, **kwargs):
    return render(request, "usuarios/singup.html", {})


def signup2(request, *args, **kwargs):
    return render(request, "usuarios/signup2.html", {})


def logout(request):
    return render(request) 

def atendimento(request, *args, **kwargs):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        assunto = request.POST['assunto']
        message = request.POST['mensagem']

    return render(request, "usuarios/atendimento.html", {})
