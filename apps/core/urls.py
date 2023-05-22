from django.urls import path
from .views import home

urlpatterns = [
    path('', home,name='home'),  # Passamos a view como parametro, após o login vem para home
]
