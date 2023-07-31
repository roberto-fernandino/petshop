from django.shortcuts import render


# Create your views here.
def home(request, *args, **kwargs):
    return render(request, "index/index.html", {})


def galeria(request, *args, **kwargs):
    return render(request, "index/galeria.html", {})


def about(request, *args, **kwargs):
    return render(request, "index/about.html", {})
