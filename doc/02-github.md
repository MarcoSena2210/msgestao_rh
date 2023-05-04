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

### Entrar no repositório do github e criar o repositrio remoto

Depois de criado, executar o comandos abaixo
````
 git remote add origin https://github.com/MarcoSena2210/msgestao_rh.git
 git push -u origin master
````

