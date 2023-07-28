from django.urls import path
from galeria import views

app_name = 'galeria'

urlpatterns = [
    path('', views.galeriaview, name='galeria')
]