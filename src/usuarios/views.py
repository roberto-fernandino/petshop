from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from usuarios import models

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
    new_atendimento = models.Atendimentos()
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        assunto = request.POST['assunto']
        message = request.POST['mensagem']
        new_atendimento.nome = nome
        new_atendimento.email = email
        new_atendimento.assunto = assunto
        new_atendimento.message = message
        new_atendimento.save()
        return redirect("usuarios:atendimento-enviado")
    return render(request, "usuarios/atendimento.html", {})


def atendimentoSubmited(request):
    return render(request, "usuarios/atendimentoSubmited.html", {})