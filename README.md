## Sobre o Script

Script simples de automação para conseguir certificados. Nesse exemplo, os dados que são inseridos são fixos, mas com um simples refatoramento consegue-se que esses valores sejam colocados pelo usuario.

## Criar virtualenv e instalar dependências

Caso não tenha o virtualenv instalado, instalar com
$ pip install virtualenv

Em seguida, criar o ambiente virtual para instalar as dependências do python para o projeto

    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt

    Ou para Windows

    $ python -m venv venv
    $ venv/Scripts/activate
    (venv) $ pip install -r requirements.txt

## Rodar script

    $ python3 tjrs.py

    Ou para Windows

    $ py tjrs.py
