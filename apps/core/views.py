from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Obriga usuario está logado
@login_required
def home(request):
    return render(request,'core/index.html')

