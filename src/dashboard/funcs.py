from usuarios.models import Atendimentos, UserCart

def AtendimentoChart():
    labels = []
    data = [0, 0]
    queryset = Atendimentos.objects.all()
    for pessoas in queryset:
        labels.append(pessoas.get_status_display())
        if pessoas.status == 'p':
            data[1] += 1
        else:
            data[0] += 1
    labels = set(labels)

    return data, list(labels)



def Carinhos_precoChart():
    labels = []
    data = []
    queryset = UserCart.objects.all()
    for carrinhos in queryset:
        labels.append(carrinhos.user.username)
        data.append(carrinhos.calculate_total_price_real())
    
    return data, labels