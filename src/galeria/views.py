from django.shortcuts import render

# Create your views here.
def galeriaview(request, *args, **kwargs):
    return render(request, "galeria.html", {})