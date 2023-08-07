from django.db import models
from usuarios.models import Account
from loja.funcs import product_image_path
from usuarios.models import UserPaymentMethod, Adress
# Create your models here.


class VariationsOptions(models.Model):
    values = models.CharField(max_length=25, default=None, blank=False, null=True)
    class Meta:
        verbose_name_plural = 'VariationsOptions'
        
class Variations(models.Model):
    variations_options_id = models.ForeignKey(VariationsOptions, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = 'Variations'

class Category(models.Model):
    category_name = models.CharField(max_length=20, null=True, blank=False, unique=True)
    variations = models.ForeignKey(Variations, on_delete=models.DO_NOTHING)
    class Meta:
        verbose_name_plural = "Categories"



class Produto(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None, blank=False, null=True)
    nome = models.CharField(max_length=25, default=None, blank=False, null=True)
    descricao = models.TextField(default=None, blank=False, null=True)
    imagem = models.ImageField(upload_to=product_image_path, default=None)
    
class ProdutoItem(models.Model):
    produto_id = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtd_stock = models.IntegerField(default=None, null=True, blank=False)
    price = models.DecimalField(default=None, blank=False, null=True, max_digits=7, decimal_places=2)


class UserCart(models.Model):
    user_id = models.ForeignKey(Account, on_delete=models.CASCADE)

class UserItems(models.Model):
    user_cart_id = models.ForeignKey(UserCart, on_delete=models.CASCADE)
    produtoItem_id = models.ForeignKey(ProdutoItem, on_delete=models.DO_NOTHING)
    qtd = models.IntegerField(default=None, blank=False, null=True) 

class ShipingMethod(models.Model):
    method = models.CharField(default=None, null=True, blank=False, max_length=30)
    valor = models.DecimalField(default=None, null=True, blank=False, max_digits=3, decimal_places=2)

class PedidoStatus(models.Model):
    status = models.CharField(max_length=15, default=None, blank=False, null=True)
    entregue = models.BooleanField(default=False)

class Pedido(models.Model):
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    user_payment_method_id = models.ForeignKey(UserPaymentMethod, on_delete=models.DO_NOTHING)
    shiping_method_id = models.ForeignKey(ShipingMethod, on_delete=models.DO_NOTHING)
    data_pedido = models.DateTimeField(auto_now_add=True)
    pedido_total = models.DecimalField(default=None, null=True, blank=False, max_digits=7, decimal_places=2)
    pedido_status_id = models.ForeignKey(PedidoStatus, on_delete=models.DO_NOTHING)
    shipping_adress = models.ForeignKey(Adress, on_delete=models.DO_NOTHING)
