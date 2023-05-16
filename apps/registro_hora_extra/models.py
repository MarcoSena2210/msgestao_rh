from django.db import models
from django.utils import timezone
from apps.funcionarios.models import Funcionario

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now)

    # Hora extra pertence a um funcionário
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo
