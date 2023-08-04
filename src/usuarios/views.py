from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from usuarios import models
from .admin import UserCrerationForm as signup_form

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
            new_user = authenticate(request, email=email, password=password2)
            if new_user is not None:
                login(request, new_user)
    
    form = signup_form()

    context = {
        "form": form  
    }
    return render(request, "usuarios/singup.html", context)


def user_view(request):
    return render(request, "usuarios/user.html", {})



def logout_view(request):
    logout(request)
    return render(request, "index/index.html", {"message": "Deslogado com sucesso!"})


def atendimento(request, *args, **kwargs):
    new_atendimento = models.Atendimentos()
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        assunto = request.POST["assunto"]
        message = request.POST["mensagem"]
        new_atendimento.nome = nome
        new_atendimento.email = email
        new_atendimento.assunto = assunto
        new_atendimento.message = message
        new_atendimento.save()
        return redirect("usuarios:atendimento-enviado")
    return render(request, "usuarios/atendimento.html", {})


def atendimentoSubmited(request):
    return render(request, "usuarios/atendimentoSubmited.html", {})
