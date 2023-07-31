from django.shortcuts import render

# Create your views here.
def lojaview(request, *args, **kwargs):
    return render(request, "loja.html", {})

def produtoview(request, *args, **kwargs):
    return render(request, 'produto.html', {})

def carrinhoview(request, *args, **kwargs):
    return render(request, 'carrinho.html', {})