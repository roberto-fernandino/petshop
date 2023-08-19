from django.shortcuts import render
import json
from .funcs import AtendimentoChart, Carinhos_precoChart
# Create your views here.


def dashboard_view(request):
    data_atendimento, labels_atendimento = AtendimentoChart()
    data_carrinho_preco, labels_carrinho_preco = Carinhos_precoChart()
    context = {
        "labels_atendimento" : json.dumps(list(labels_atendimento)),
        "data_atendimento": json.dumps(data_atendimento),
        "data_carrinho_preco": json.dumps(data_carrinho_preco),
        "labels_carrinho_preco": json.dumps(labels_carrinho_preco),
    }
    return render(request, "dashboard/dashboard.html", context)
