from django.contrib import admin
from loja.models import Produto, Category, Pedido, UserItems, Variations, VariationsOptions
# Register your models here.



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'category')
    ordering = ['nome']
    search_fields = ['nome']


@admin.register(UserItems)
class UserItemsAdmin(admin.ModelAdmin):
    search_fields = ['produto__nome']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]
    search_fields = ["category_name"]

@admin.register(Variations)
class VariationsAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(VariationsOptions)
class VariationsOptionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'values']