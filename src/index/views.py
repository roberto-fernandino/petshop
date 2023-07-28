from django.shortcuts import render

# Create your views here.
def homeview(request, *args, **kwargs):
    return render(request, "index.html", {})