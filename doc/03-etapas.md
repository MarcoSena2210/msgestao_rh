1-Criando o app empresa

Na raiz do projeto, vamos criar um pakage python, chamado "apps"

Ativar a virual env, como estamos no terminal gitbash, deve ser ativado assim:
`
msena@DESKTOP-NU65P6S MINGW64 /d/DevDjango/msgestao_rh (master)
````
. venv/Scripts/activate
````

output
````
(venv) 
````


### Listando todos comandos disponiveis pelomanage.py
````
 python manage.py
````
Output 
````
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    optimizemigration
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
(venv) 
````



### 1-Criando o app empresas
(venv) D:\dev\msgestaorh>
````
    python manage.py startapp empresas
````

Dica: Será criado uma nova pasta chamada empresas, com a estrutura de arquivos 
do app.

#### Obs:
     Mova a pasta empresas para pasta apps 

### 2-Registrar o app empresa no settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    ....
    'apps.empresas',
]

Criar o model Empresa no arquivo empresa\models.py
from django.db import models


class Empresa(models.Model):
    nome = models.CharField("help_text=Nome da Empresa",
                            max_length=100, blank=False)
Rodar o makemigrations
(venv) D:\dev\msgestaorh>