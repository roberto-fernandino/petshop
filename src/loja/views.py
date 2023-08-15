from django.shortcuts import render, redirect
from loja.models import Produto, Category, TosaType, BanhoType, Banho, Tosa
from django.http import HttpResponseRedirect
import stripe
from loja.forms import TosaForm, BanhoForm
from maindjango.settings import STRIPE_PUBLIC_KEY
from loja.funcs import SearchProductsToPaymentGateway
from usuarios.models import UserCart, UserCartItems
from django.contrib.auth.decorators import login_required

# stripe api key
stripe.api_key = STRIPE_PUBLIC_KEY


# Create your views here.
def lojaview(request, *args, **kwargs):
    produtos = Produto.objects.all()
    categorias = Category.objects.all()

    # category filter
    categoria_id = request.GET.get("categoria")
    if categoria_id:
        produtos = produtos.filter(category=categoria_id)

    # nome filter
    nome = request.GET.get("nome")
    if nome:
        produtos = produtos.filter(nome__icontains=nome)

    # filtra por preco maximo
    preco_max = request.GET.get("preco_max")
    if preco_max:
        produtos = produtos.filter(preco__lte=float(preco_max) * 100)

    return render(
        request,
        "loja/loja.html",
        {
            "produtos": produtos,
            "categorias": categorias,
            "nome": nome,
            "preco": preco_max,
        },
    )


@login_required
def add_cart(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    cart, _ = UserCart.objects.get_or_create(user=request.user)
    cart_item, created = UserCartItems.objects.get_or_create(cart=cart, produto=produto)
    quantidade = int(request.POST.get("quantidade", 1))
    produto.estoque -= quantidade
    produto.save()
    if not created:
        cart_item.quantidade += quantidade
    else:
        cart_item.quantidade = quantidade

    cart_item.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def remove_cart(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    cart, _ = UserCart.objects.get_or_create(user=request.user)
    cart_items = UserCartItems.objects.get(cart=cart, produto=produto)
    quantidade = int(request.POST.get("quantidade"))
    if quantidade == cart_items.quantidade:
        cart_items.delete()
    else:
        produto.estoque += quantidade
        cart_items.quantidade -= quantidade
        produto.save()
        cart_items.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def remove_all_cart(request, produto_id):
    produto = Produto.objects.get(pk=produto_id)
    cart = UserCart.objects.get(user=request.user)
    cart_items = UserCartItems.objects.get(cart=cart, produto=produto)
    cart_items.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def create_checkout_session():
    def post(self, *args, **kwargs):
        stripe.checkout.Session.create(
            payment_method_types=["card"],
            sucess_url="",
            line_items=[
                {
                    "price_data": {
                        "currency": "brl",
                    }
                }
            ],
        )


@login_required
def tosa(request):
    categorias = TosaType.objects.all()
    categorias_banho = BanhoType.objects.all()
    usuario = request.user
    if request.method == "POST":
        tosa_form = TosaForm(request.POST)
        tosa_id = request.POST.get("tosa-type")
        tosa_instance = TosaType.objects.get(pk=tosa_id)
        banho_form = (
            BanhoForm(request.POST) if request.POST.get("banho") == "on" else None
        )

        if tosa_form.is_valid():
            tosa = tosa_form.save(commit=False)
            nome_pet = tosa_form.cleaned_data["pet"]
            data = tosa_form.cleaned_data["data"]
            tosa.user = usuario
            tosa.type = tosa_instance
            tosa.save()

            if banho_form and banho_form.is_valid():
                banho_id = request.POST.get("banho-type")
                banho_instance = BanhoType.objects.get(pk=banho_id)
                banho = banho_form.save(commit=False)
                banho.user = usuario
                banho.type = banho_instance
                banho.data = data
                banho.pet = nome_pet
                banho.save()

        return redirect("loja:tosa_marcada")

    tosa_form = TosaForm()
    banho_form = BanhoForm()
    context = {
        "categorias": categorias,
        "categorias_banho": categorias_banho,
        "form": tosa_form,
        "banhoform": banho_form,
    }
    return render(request, "loja/tosa.html", context)


@login_required
def tosa_marcada(request):
    return render(request, "loja/tosamarcada.html")


@login_required
def banho(request):
    categorias = BanhoType.objects.all()
    categorias_tosa = TosaType.objects.all()
    usuario = request.user
    if request.method == "POST":
        banho_form = BanhoForm(request.POST)
        tosa_form = TosaForm(request.POST) if request.POST.get("tosa") == "on" else None
        banho_id = request.POST.get("banho-type")
        banho_instance = BanhoType(pk=banho_id)

        if banho_form.is_valid():
            banho = banho_form.save(commit=False)
            nome_pet = banho_form.cleaned_data["pet"]
            data = banho_form.cleaned_data["data"]
            banho.user = usuario
            banho.type = banho_instance
            banho.save()

            if tosa_form and tosa_form.is_valid():
                tosa_id = request.POST.get("tosa-type")
                tosa_instance = TosaType.objects.get(pk=tosa_id)
                tosa = tosa_form.save(commit=False)
                tosa.pet = nome_pet
                tosa.user = usuario
                tosa.type = tosa_instance
                tosa.data = data
                tosa.save()

            return redirect("loja:banho_marcado")

    banho_form = BanhoForm()

    context = {
        "categorias": categorias,
        "form": banho_form,
        "categorias_tosa": categorias_tosa,
    }
    return render(request, "loja/banho.html", context)


@login_required
def banho_marcado(request):
    return render(request, "loja/banhomarcado.html")
