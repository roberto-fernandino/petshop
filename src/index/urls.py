from django.urls import path
from index import views

# URLS AQUIII

app_name = 'home'


urlpatterns = [
    path('', views.homeview, name='home')
]
