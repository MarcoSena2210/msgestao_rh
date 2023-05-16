# Definindo os relacionamentos:

## Chaves estragiras:
### Funcionarios tem vinculo com usuario (do django) podendo reaproveirar muitas caracteristicas de usuario
    
    
    # Para deletar o usuario precisa excluir o funcionário 
    # primeiro 
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    #Um funcionarios pode ter uma lista de departamentos
    departamentos = models.ManyToManyField(Departamento)        
    
    # Um funcionario pertence a uma empresa e só veroa tudo dessa empresa
    # Se precisar ter mais de uma, cria-se um login para cada uma empresa
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

arquivo `apps/funcionarios/models.py'

````
from django.db import models
from django.contrib.auth.models import User
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

```` 
## Um documento pertence a um funcionario e pode ser deletado um documento sem 
## que seja excluído o funcionário

apps/documentos/models.py
````commandline
from django.db import models
from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.descricao

````

## Hora extra
## Hora extra pertence a um funcionário

apps/registro_hora_extra/models.py
````
from django.db import models
from apps.funcionarios.models import Funcionario


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    def __str__(self):
        return self.motivo
````

Dica: Deu alguns erros ao tentar rodar o makemigrations e migrate, pois já existiam alguns 
cadastrados, precisei associar ao registro 1.
Exemplo: O funcionario funcionario que já existia ficou associado a empresa 1, ao departamento 1 e
ao user =1

Deletei o app ducmentos pois estava dando erros também. Posteriormente iremos recria-lo.
