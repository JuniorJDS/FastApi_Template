# Template para uma API utilizando FastAPI

> O propósito deste template é ter uma estrutura e agilizar o processo de criação das APIs.

## Estrutura do Projeto
``` 
├── FastAPI_Template
|   ├── app
|   |     ├── core
|   |     |  ├── config.py
|   |     |  ├── security.py
|   |     ├── crud
|   |     ├── models
|   |     ├── routers
|   |     |   ├── v1          
|   |     ├── schemas
|   |     ├── db.py
|   |     ├── main.py
|   ├── tests
|   ├── README.md
|   ├── requirements.txt
└── ...

```

### Criando um ambiente Virtual e Instalando os requirements

```
$ python3 -m venv env

$ source env/bin/activate

$ pip3 install --upgrade pip

$ pip3 install -r requirements.txt

```

### Como rodar?

```
$ uvicorn app.main:app --reload

```
