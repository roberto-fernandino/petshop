from django.db import models
from usuarios.models import Account
from loja.funcs import product_image_path

# Create your models here.

class Category(models.Model):
    nome = models.CharField(max_length=60, default=None, blank=False, null=False)
    def __str__(self) -> str:
        return f"{self.nome}"
    class Meta:
        verbose_name_plural = 'Categories'


class Produto(models.Model):
    nome = models.CharField(max_length=50, default="Produto", unique=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    descricao = models.TextField()
    img = models.ImageField(upload_to=product_image_path)
    estoque = models.IntegerField(default=0, null=False, blank=False)