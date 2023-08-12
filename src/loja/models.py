import stripe
from django.db import models
from loja.funcs import product_image_path
from maindjango.settings import STRIPE_PUBLIC_KEY
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

    def __str__(self) -> str:
        return f"{self.nome}| Cat:{self.category} | R${(self.preco)/100}"


