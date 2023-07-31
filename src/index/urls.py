from django.urls import path
from index import views

# URLS AQUIII

app_name = "home"


urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("galeria", views.galeria, name="galeria"),
]
