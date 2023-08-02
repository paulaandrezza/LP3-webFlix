# Projeto WebFlix com Django

## 📑 Sobre o Projeto
Site voltado para classificação de filmes por genêro, mais assistidos, etc.
Uma plataforma parecida com o streaming Netflix

### As tarefas serão executadas na seguinte ordem:
1. HomePage principal
2. Criar login e criar conta (usuário e autenticação)
    - Email
    - Username
    - Senha
    - Filmes já vistos
    - Entrar no perfil do usuário
3. Filmes
    - Thumb
    - Título
    - Descrição
    - Categoria
    - Quantidade de visualizações
    - Data de criação
    - episódios
      - videos
      - título
    - Barra de pesquisa


## ✨ Passo a passo

### 01.08.2023
Para iniciar o projeto é preciso instalar o django, no termina digite:
```commandline
pip install django
```
Em seguida para iniciar o projeto:
```commandline
django-admin start-project webflix .
```
Para abrir o projeto, no terminal digite, ele irá rodar na porta `http://127.0.0.1:8000/` ou `http://localhost:8000/`:
```commandline
python manage.py runserver
```