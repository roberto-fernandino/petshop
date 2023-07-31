from django.contrib import admin
from usuarios.models import Atendimentos

# Register your models here.

@admin.action(description="Marque pedidos selecionados como respondidos")
def set_respondidos(modeladmin, request, queryset):
    queryset.update(status='r')

class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'assunto', 'status', 'data']
    ordering = ['data']
    actions =[set_respondidos]

admin.site.register(Atendimentos, AtendimentoAdmin)