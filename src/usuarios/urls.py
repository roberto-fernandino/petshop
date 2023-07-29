from django.urls import path
from usuarios import views


# URLS AQUI

app_name = 'usuarios'

urlpatterns = [
    path('login', views.loginview, name='login'),
    path('signup', views.signupview, name='signup'),
    path('signupfinal', views.signupview2, name='signup2'),
    path('atendimento', views.atendimento, name='atendimento'),
    ]