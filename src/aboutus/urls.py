from django.urls import path
from aboutus import views

# urls aqui

app_name = 'aboutus'

urlpatterns = [
    path('', views.aboutview, name='aboutus')
]