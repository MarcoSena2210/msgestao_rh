### Configurar o caminho do gitbash no pycharm


````
or create a new repository on the command line
echo "# msgestao_rh" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/MarcoSena2210/msgestao_rh.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/MarcoSena2210/msgestao_rh.git
git branch -M main
git push -u origin main
````




### No pycharm criar o arquivo .gitignore e acrescentar os arquivos que não 
deve subir para o git
arquivo: .gitignore
````
.idea/
*sqlite3
venv/
````

### Abrir o terminal no pycharm e iniciar o git
````
git init
````

git add .

### Fazendo o commit
````
git commit -m "First commit"
````

<<<<<<< HEAD
### Entrar no github e criar o repositório remoto
=======
### Entrar no repositório do github e criar o repositrio remoto
>>>>>>> 804d63794167a5cb7f3a0b731af2eb9275d27607

Depois de criado, executar o comandos abaixo
````
 git remote add origin https://github.com/MarcoSena2210/msgestao_rh.git
 git push -u origin master
````

<<<<<<< HEAD
### Fazendo o 2º backup no git
#### Usamos o git status para verificar o que foi mudado
````
git status
````
Outpt
````
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   .gitignore
        modified:   doc/02-github.md
        modified:   doc/03-etapas.md
        modified:   msgestao_rh/__pycache__/settings.cpython-310.pyc
        modified:   msgestao_rh/settings.py

```` 

Como não queremos enviar a **msgestao_rh/__pycache__/settings.cpython-310.pyc**
e não estamos tratando no .gitignore, vamos adicionar uma mudança de cada vez.

````
 git add .gitignore
 git add apps
 git add msgestao_rh/settings.py
 git add doc
 git commit -m "#002-Criando a app empresas"
 git push origin master
````

Output final
````
Enumerating objects: 25, done.
Counting objects: 100% (25/25), done.
Delta compression using up to 4 threads
Compressing objects: 100% (19/19), done.
Writing objects: 100% (20/20), 5.67 KiB | 1.13 MiB/s, done.
Total 20 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/MarcoSena2210/msgestao_rh.git
   ccc612f..804d637  master -> master

msena@DESKTOP-NU65P6S MINGW64 /d/DevDjango/msgestao_rh (master)
````


=======
>>>>>>> 804d63794167a5cb7f3a0b731af2eb9275d27607
