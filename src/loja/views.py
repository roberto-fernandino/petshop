from django.shortcuts import render, redirect
from loja.models import Produto, Category, TosaType, Tosa
from django.http import HttpResponseRedirect
import stripe
from loja.forms import TosaForm
from maindjango.settings import STRIPE_PUBLIC_KEY
from loja.funcs import SearchProductsToPaymentGateway
from usuarios.models import UserCart, UserCartItems
from django.contrib.auth.decorators import login_required

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
        produtos = produtos.filter(preco__lte=float(preco_max) * 100)
    
    return render(request, "loja/loja.html", {"produtos": produtos, "categorias": categorias, 'nome': nome, 'preco': preco_max})

def produtoview(request, *args, **kwargs):
    return render(request, 'loja/produto.html', {})

@login_required
def carrinhoview(request, *args, **kwargs):
    return render(request, 'carrinho.html', {})

@login_required
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

@login_required
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


@login_required
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

@login_required
def tosa(request):
    categorias = TosaType.objects.all()
    if request.method == 'POST':
        tosa_form = TosaForm(request.POST)
        tosa_id = request.POST.get('tosa-type')
        tosa_instance = TosaType.objects.get(pk=tosa_id)
        if tosa_form.is_valid():
            tosa = tosa_form.save(commit=False)
            tosa.user = request.user
            tosa.type = tosa_instance
            tosa.save()
            return redirect('loja:tosa_marcada')
    tosa_form = TosaForm()
    context = {
        'categorias': categorias,
        'form': tosa_form,
    }
    return render(request, 'loja/tosa.html', context)



@login_required
def tosa_marcada(request):
    return render(request, 'loja/tosamarcada.html')