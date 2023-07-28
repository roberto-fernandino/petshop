from django.urls import path
from index import views

# URLS AQUIII

app_name = 'index'


urlpatterns = [
    path('', views.homeview, name='Home')
]
