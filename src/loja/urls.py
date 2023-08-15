from django.urls import path
from loja import views


app_name = 'loja'

# urls AQUI


urlpatterns = [
    path('', views.lojaview, name='loja'),
    path('add-cart/<int:produto_id>/', views.add_cart, name='add-cart'),
    path('remove-cart/<int:produto_id>/', views.remove_cart, name='remove-cart'),
    path('remove-all-cart/<int:produto_id>', views.remove_all_cart, name='remove-all-cart'),
    path('tosa', views.tosa, name='tosa'),
    path('tosa/marcada', views.tosa_marcada, name='tosa_marcada'),
    path('banho', views.banho, name='banho'),
    path('banho/marcado', views.banho_marcado, name='banho_marcado'),
]