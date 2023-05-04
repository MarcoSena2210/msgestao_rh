from django.db import models
from django.utils import timezone


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome completo")
    data_criacao = models.DateTimeField(default=timezone.now)
    cpf = models.CharField(verbose_name="CPF",max_length=11)
    data_nascimento = models.DateField(verbose_name="Data de nascimento",auto_now=False)
    email = models.EmailField(
        verbose_name="E-mail do funcionario",
        max_length=254,
        unique=True,
    )


    def __str__(self):
        return self.nome

    def get_cpf(self):
        cpf = self.cpf
        cpf_mascarado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
        return cpf_mascarado




