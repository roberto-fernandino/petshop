from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from usuarios import models
from .admin import UserCrerationForm as signup_form
from usuarios.forms import AtendimentoForm
from usuarios.mail import EnviaSigunupEmail

# Create your views here.

def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("usuarios:usuario")
    elif request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, "usuarios/user.html", {
                "message": "Bem vindo de volta "
            })
        else:
            return render(
                request, "usuarios/login.html", {"message": "Email ou senha invalidos"}
            )
    return render(request, "usuarios/login.html", {})


def login_sucess(request):
    if request.user.is_authenticated:
        return render(request, "usuarios/loginsucess.html")


def signup(request, *args, **kwargs):
    if request.method == "POST":
        form = signup_form(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data['email']
            password2 = form.cleaned_data['password2']
            username = form.cleaned_data['username']
            new_user = authenticate(request, email=email, password=password2)
            if new_user is not None:
                login(request, new_user)
                log = EnviaSigunupEmail(email=email, username=username)
                new_log = models.EmailErrorsLog()
                new_log.log = log
                new_log.email = email
                new_log.save()
                return redirect('usuarios:signupsucess')
        else:
            return render(request, "usuarios/signup.html", {"form": form})
            

    form = signup_form()
    context = {
        "form": form,  
        
    }
    return render(request, "usuarios/signup.html", context)


def user_view(request):
    return render(request, "usuarios/user.html", {})

def signup_sucess_view(request):
    return render(request, "usuarios/signupsucess.html", {})

def logout_view(request):
    logout(request)
    return render(request, "index/index.html", {"message": "Deslogado com sucesso!"})


def atendimento(request, *args, **kwargs):
    if request.method == "POST":
        form = AtendimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios:atendimento-enviado")
        else:
            return render(request, "usuarios/atendimento.html")
    
    form = AtendimentoForm()
    
    return render(request, "usuarios/atendimento.html", {"form": form})


def atendimentoSubmited(request):
    return render(request, "usuarios/atendimentoSubmited.html", {})
