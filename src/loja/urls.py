from django.urls import path
from loja import views


app_name = 'loja'

# urls AQUI


urlpatterns = [
    path('', views.lojaview, name='loja'),
    path('produto', views.produtoview, name='produto'),
    path('add-cart/<int:produto_id>/', views.add_cart, name='add-cart'),
    path('remove-cart/<int:produto_id>/', views.remove_cart, name='remove-cart'),

]