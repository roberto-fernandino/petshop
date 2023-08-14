from django.shortcuts import render, redirect
from loja.models import Produto, Category
from django.http import HttpResponseRedirect
import stripe
from maindjango.settings import STRIPE_PUBLIC_KEY
from loja.funcs import SearchProductsToPaymentGateway
from usuarios.models import UserCart, UserCartItems

#stripe api key
stripe.api_key = STRIPE_PUBLIC_KEY


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
    return render(request, 'loja/produto.html', {})

def carrinhoview(request, *args, **kwargs):
    return render(request, 'carrinho.html', {})

def add_cart(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    cart, _ = UserCart.objects.get_or_create(user=request.user)
    cart_item, created = UserCartItems.objects.get_or_create(cart=cart , produto=produto)
    quantidade = int(request.POST.get('quantidade', 1))
    produto.estoque -= quantidade
    produto.save()
    if not created:
        cart_item.quantidade += quantidade
    else:
        cart_item.quantidade = quantidade
    
    cart_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def remove_cart(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    cart, _ = UserCart.objects.get_or_create(user=request.user)
    cart_items = UserCartItems.objects.get(cart=cart, produto=produto)
    quantidade = int(request.POST.get('quantidade'))
    produto.estoque += quantidade
    cart_items.quantidade -= quantidade
    produto.save()
    cart_items.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", '/'))

def create_checkout_session():
    def post(self, *args, **kwargs):
        stripe.checkout.Session.create(
            payment_method_types=['card'],
            sucess_url='',
            line_items=[
                {
                    'price_data':{
                        'currency': 'brl',
    
                    }
                }
            ],
        )