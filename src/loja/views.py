from django.shortcuts import render
from loja.models import Produto, Category

# Create your views here.
def lojaview(request, *args, **kwargs):
    produtos = Produto.objects.all()
    categorias = Category.objects.all()

    #category filter
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        produtos = produtos.filter(category=categoria_id)
    
    #nome filter
    nome = request.GET.get('nome')
    if nome:
        produtos = produtos.filter(nome__icontains=nome)
    
    #filtra por preco maximo
    preco_max = request.GET.get("preco_max")
    if preco_max:
        produtos = produtos.filter(preco__lte=float(preco_max))
    
    


    return render(request, "loja.html", {"produtos": produtos, "categorias": categorias})

def produtoview(request, *args, **kwargs):
    return render(request, 'produto.html', {})

def carrinhoview(request, *args, **kwargs):
    return render(request, 'carrinho.html', {})