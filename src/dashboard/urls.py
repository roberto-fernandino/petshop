from django.urls import path
from dashboard.views import *


app_name = "dashboard"

urlpatterns = [
    path("", dashboard_view, name='dashboard')
]
