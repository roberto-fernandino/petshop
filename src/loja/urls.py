from django.urls import path
from loja import views


app_name = 'loja'

# urls AQUI


urlpatterns = [
    path('', views.lojaview, name='loja'),
    path('', views.produtoview, name='produto'),
        
        #no futuro ->  path(f'{nomeproduto}', views.produtoview, name='loja')


]