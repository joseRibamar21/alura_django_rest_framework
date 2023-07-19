## Instalação


### Ambiente Virual

Crie uma pasta para manter seu código e acessando essa pasta em um terminal, crie um ambiente virtual com o seguinte comando:

```
    python3 -m venv ./venv
```

Ative seu ambiente virtual com o seguinte comando (MAC e Linux):

```
    source venv/bin/activate
```

Em caso de Windows, utilize o comando

```
    venv\Scripts\activate.bat
```

### Instale o Django nesse ambiente virtualizado:

```
    pip install django
```

### ADMIN

Crie um projeto chamado setup utilizando o Django admin, para manter toda configuração de nossa aplicação:

```
    django-admin startproject setup .
```

Para finalizar a configuração do ambiente, na pasta setup, altere no arquivo settings.py o idioma e o horário que usaremos na aplicação, incluindo as seguintes linhas de código:

```
    LANGUAGE_CODE = 'pt-br'
    TIME_ZONE = 'America/Sao_Paulo'
```

```
    python manage.py startapp [nome_do_projeto]
```

## Rodar a aplicação

```
    python manage.py runserver
```

## Instalando Django REST Framework

```
    pip install djangorestframework
    pip install markdown
```

## Criar Migrates

```
    python manage.py makemigrations
```

## Criar Migrates

<code>
python manage.py migrate
<code>
