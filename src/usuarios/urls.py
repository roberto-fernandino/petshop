from django.urls import path
from . views import *

# URLS AQUI

app_name = 'usuarios'

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('signup', signup, name='signup'),
    path('signupfinal', signup2, name='signup2'),
    path('atendimento', atendimento, name='atendimento'),
    ]