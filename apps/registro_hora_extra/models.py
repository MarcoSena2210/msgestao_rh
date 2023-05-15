from django.db import models
from django.utils import timezone

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.motivo
