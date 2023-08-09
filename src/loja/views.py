from django.shortcuts import render
from loja.models import Produto

# Create your views here.
def lojaview(request, *args, **kwargs):
    produtos = Produto.objects.all()
    return render(request, "loja.html", {"produtos": produtos})

def produtoview(request, *args, **kwargs):
    return render(request, 'produto.html', {})

def carrinhoview(request, *args, **kwargs):
    return render(request, 'carrinho.html', {})