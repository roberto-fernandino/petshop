from django.urls import path
from .views import *

# URLS AQUI

app_name = 'usuarios'

urlpatterns = [
    path('login', login_view, name='login'),
    path('login/logged-in', login_sucess, name="login_sucess"),
    path('usuario', user_view, name='usuario'),
    path('logout', logout_view, name='logout'),
    path('signup', signup, name='signup'),
    path('atendimento', atendimento, name='atendimento'),
    path('atendimento/enviado', atendimentoSubmited, name='atendimento-enviado'),
]