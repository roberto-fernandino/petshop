from django.contrib import admin
from loja.models import Produto, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque', 'category']
    list_filter = ['preco', 'estoque']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nome']

admin.site.register(Produto, ProductAdmin)
admin.site.register(Category, CategoryAdmin)