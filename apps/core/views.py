from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario

# Obriga usuario está logado
# Neste ponto ao se logar, o sistema irá enviar os dados
# relativo a que empresa o usuário pertence.Para isso precisa se comunicar com
# app funcionario


# Precisamos saber o user e a empressa
@login_required
def home(request):
    data = {} # Criamos um dicionario
    data['usuario'] = request.user
    return render(request,'core/index.html',data)

