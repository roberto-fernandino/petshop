from django.urls import path
from loja import views


app_name = 'loja'

# urls AQUI


urlpatterns = [
    path('', views.lojaview, name='loja'),
    path('produto', views.produtoview, name='produto'),
    path('carrinho', views.carrinhoview, name='carrinho'),

        
        #no futuro ->  path(f'{nomeproduto}', views.produtoview, name='loja')


]