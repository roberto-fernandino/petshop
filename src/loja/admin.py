from django.contrib import admin
from .models import Produto
# Register your models here.



class ProdutoAdmin(admin.ModelAdmin):
    list_display = ["nome_produto", "setor"]
    ordering = ["preco"]
    list_filter = ["preco", "setor"]
    search_fields = ["nome_produto"]
    filter_horizontal = []

admin.site.register(Produto, ProdutoAdmin)