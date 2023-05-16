from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home),  # Passamos a view como parametro
]
