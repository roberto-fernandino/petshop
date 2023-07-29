from django.shortcuts import render

# Create your views here.
def aboutview(request):
    return render(request, "aboutus.html", {})