import stripe
from django.db import models
from loja.funcs import product_image_path
from maindjango.settings import STRIPE_PUBLIC_KEY
from django.apps import apps
import sqlite3

stripe.api_key = STRIPE_PUBLIC_KEY


# Create your models here.


class Category(models.Model):
    nome = models.CharField(max_length=60, default=None, blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.nome}"

    class Meta:
        verbose_name_plural = "Categories"


class Produto(models.Model):
    nome = models.CharField(max_length=50, default="Produto", unique=True)
    preco = models.IntegerField(default=0)  # cents
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    descricao = models.TextField()
    img = models.ImageField(upload_to=product_image_path)
    estoque = models.IntegerField(default=0, null=False, blank=False)

    def preco_em_real(self):
        return f"{(self.preco) / 100 }"

    def __str__(self) -> str:
        return f"{self.nome}| Cat:{self.category} | R${(self.preco)/100}"


class porte(models.Model):
    porte = models.CharField(default=None, blank=False, null=True, max_length=30)

    def __str__(self) -> str:
        return f"{self.porte}"


class TosaType(models.Model):
    name = models.CharField(default=None, blank=False, null=False, max_length=30)
    preco = models.FloatField()
    porte = models.ForeignKey(porte, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.porte} R${self.preco}"

class BanhoType(models.Model):
    name = models.CharField(default=None, blank=False, null=False, max_length=30)
    preco = models.FloatField()
    porte = models.ForeignKey(porte, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return f"{self.name} {self.porte} R${self.preco}"

class Banho(models.Model):
    user = models.ForeignKey("usuarios.Account", on_delete=models.CASCADE, blank=False, null=True, related_name="banho")
class Tosa(models.Model):
    user = models.ForeignKey(
        "usuarios.Account", on_delete=models.CASCADE, blank=False, null=True, related_name='tosa'
    )
    pet = models.CharField(default=None, max_length=30, blank=False, null=True)
    type = models.ForeignKey(TosaType, on_delete=models.CASCADE)
    data = models.DateTimeField(unique=True)