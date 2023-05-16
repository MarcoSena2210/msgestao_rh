from django.utils import timezone
from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=70)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome
