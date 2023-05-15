from django.db import models
from django.utils import timezone

class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.descricao

