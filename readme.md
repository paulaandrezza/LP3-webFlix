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

### 08.08.2023

Para iniciar a o app filme, no terminal digite:

```
django-admin startapp filme
```

Após iniciar o app filme precisa adiciona-lo a INSTALLED_APPS em settings.py

Para fazer migrações:

```
python manage.py migrate
```

Para criar um superusuario:

```
python manage.py createsuperuser
```

### 15.08.2023

Mudar as configurações no arquivo settings.py para:

```
LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'
```

E adicionar depois de `STATIC_URL = 'static/'`:

```
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

```

Na raiz criar a seguinte sequencia de pastas:

```
├── media
│   └── ...
│
└── static
    └── css
    └── images
    └── js
```
