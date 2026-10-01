# FastAPI Blog API

API REST desenvolvida com **Python e FastAPI** para gerenciamento de usuários e artigos, utilizando **MySQL** como banco de dados e **SQLAlchemy** para o mapeamento e comunicação com o banco.

O projeto foi desenvolvido com foco em praticar a construção de APIs modernas, organização de código, operações CRUD, autenticação, validação de dados e integração com banco de dados relacional.

> **Status:** Projeto desenvolvido para estudo e portfólio.  
> **Execução atual:** Localmente, utilizando FastAPI/Gunicorn.  
> **Deploy:** O projeto não está atualmente hospedado em produção.

---

## Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- Gunicorn
- Uvicorn
- REST API
- Git e GitHub

---

## Sobre o projeto

O **FastAPI Blog API** é uma aplicação backend desenvolvida para colocar em prática conceitos de desenvolvimento de APIs REST utilizando Python.

A aplicação possui recursos relacionados ao gerenciamento de:

- Usuários
- Artigos
- Autenticação
- Banco de dados
- Operações CRUD
- Validação de dados
- Segurança e controle de acesso

O projeto foi estruturado de forma modular, separando as responsabilidades da aplicação em diferentes diretórios e arquivos.

Essa organização facilita a manutenção do código e permite que novos recursos sejam adicionados futuramente.

---

## Arquitetura do projeto

A aplicação possui uma arquitetura dividida em diferentes camadas:

```text
                         CLIENTE
                            │
                            ▼
                     ┌─────────────┐
                     │   FastAPI   │
                     └──────┬──────┘
                            │
                            ▼
                     ┌─────────────┐
                     │   Routers   │
                     │  Endpoints  │
                     └──────┬──────┘
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
         ┌─────────────┐         ┌─────────────┐
         │   Schemas   │         │    Models   │
         │  Pydantic   │         │  SQLAlchemy │
         └─────────────┘         └──────┬──────┘
                                        │
                                        ▼
                                ┌─────────────┐
                                │    MySQL    │
                                └─────────────┘
