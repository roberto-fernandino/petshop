from django.contrib import admin
from loja.models import Produto, Category, Tosa, TosaType

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['nome', 'preco', 'estoque', 'category']
    list_filter = ['preco', 'estoque']
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['nome']

class TosaTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'preco', 'porte']
    list_filter = ['name']
    fieldsets = [
        (None, {"fields": ['name', 'porte']}),
        ("Preco", {"fields": ['preco']})
    ]

class TosaAdmin(admin.ModelAdmin):
    list_display = ['type', 'user', 'data', 'pet']
    list_filter = ['user', 'data']
    fieldsets = [
        (None, {"fields" : ['user', 'type', 'pet']}),
        ("Information", {"fields": ['data']})
    ]

admin.site.register(TosaType, TosaTypeAdmin)
admin.site.register(Tosa, TosaAdmin)
admin.site.register(Produto, ProductAdmin)
admin.site.register(Category, CategoryAdmin)