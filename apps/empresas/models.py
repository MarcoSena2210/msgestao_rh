from django.db import models
from django.urls import reverse
from django.utils import timezone


class Empresa(models.Model):
    STATUS_EMPRESA = [
        ("AGUARDANDO", "Aguardando autorização"),
        ("ATIVA", "Ativa, pleno funcionamento"),
        ("INATIVA","Inativa"),
    ]
    nome = models.CharField(max_length=100, help_text='Nome da Empresa')
    data_criacao = models.DateTimeField(default=timezone.now)
    status = models.CharField(verbose_name="Status",max_length=25,
                              choices=STATUS_EMPRESA,default="AGUARDANDO",)


    def __str__(self):
        return self.nome

    def get_absolute_url(self):
       return reverse('home')
