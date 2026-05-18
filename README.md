
# 📌 Pendências API

A Pendências API é um projeto desenvolvido com FastAPI com o objetivo de gerenciar tarefas e pendências do dia a dia de forma simples, prática e estruturada. A ideia é simular um sistema real de organização pessoal, permitindo evoluir o projeto aos poucos com novas funcionalidades como criação, listagem, atualização e remoção de pendências.

O projeto também foi pensado como ambiente de aprendizado e prática de conceitos importantes como construção de APIs REST, testes automatizados, boas práticas de código e ferramentas do ecossistema Python.

---

## 🚀 Tecnologias utilizadas

- Python 3.14+
- FastAPI
- Pytest
- Coverage (cobertura de código)
- Ruff (lint e formatação)
- Taskipy (automação de comandos)
- Poetry (gerenciamento de dependências)

---

## 📂 Estrutura do projeto

pendencias/  
├── pendencias/  
│   ├── __init__.py  
│   └── app.py  
├── tests/  
│   ├── __init__.py  
│   └── test_app.py  
├── htmlcov/  
├── pyproject.toml  
├── poetry.lock  
└── README.md  

---

## ▶️ Executando a aplicação

Instale as dependências:

poetry install

Execute a API:

task run

A aplicação ficará disponível em:

http://127.0.0.1:8000

Documentação interativa:

http://127.0.0.1:8000/docs

---

## 🧪 Executando os testes

Rode:

task test

Esse comando executa:

- lint com Ruff  
- testes com pytest  
- geração de cobertura de código  
- criação do relatório HTML  

---

## 📊 Cobertura de código

Após rodar os testes, abra o relatório com:

start htmlcov\\index.html

---

## ✅ Exemplo de endpoint atual

@app.get('/')
def read_root():
    return {'message': 'Hello World!'}

Resposta esperada:

{
  "message": "Hello World!"
}

---

## ✅ Exemplo de teste

def test_root_dev_retornar_hello_world():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World!'}

---

## 🧹 Lint e formatação

Rodar lint:

task lint

Formatar código:

task format

---

## 🧠 Objetivo do projeto

A ideia é evoluir essa API para um sistema completo de gerenciamento de pendências, permitindo:

- criar pendências  
- listar pendências  
- atualizar pendências  
- remover pendências  
- marcar como concluídas  
- definir prioridades  
- adicionar prazos  

Além disso, o projeto ajuda a praticar:

- construção de APIs REST  
- testes automatizados  
- qualidade de código  
- organização de projetos  

---

## ⚠️ Observações

- A pasta htmlcov é gerada automaticamente  
- Não deve ser editada manualmente  
- Se algo estranho acontecer, limpe o cache:

rmdir /s /q htmlcov  
rmdir /s /q .pytest_cache  

- Sempre salve os arquivos antes de rodar os testes 😉

---

## 👩‍💻 Autora

Vanessa Targino
