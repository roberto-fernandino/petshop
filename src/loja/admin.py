from django.contrib import admin
from loja.models import Produto

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque']
    list_filter = ['preco', 'estoque']
    

admin.site.register(Produto, ProductAdmin)