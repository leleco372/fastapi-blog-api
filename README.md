
# API RESTful - Plataforma de Artigos e Utilizadores

Bem-vindo ao repositório da nossa API RESTful. Este projeto foi desenvolvido com foco em alta performance, segurança e escalabilidade, fornecendo um sistema completo para a gestão de utilizadores e artigos. A API foi estruturada seguindo as melhores práticas de desenvolvimento, garantindo uma manutenção simplificada e código limpo.

---

## 🏗️ Estrutura do Projeto

O projeto segue uma arquitetura modular, separando responsabilidades de forma clara:

* **`api/v1/`**: Contém os *routers* (rotas) da aplicação.
  * `endpoints/artigo.py`: Rotas relacionadas com a gestão de artigos (CRUD).
  * `endpoints/usuario.py`: Rotas relacionadas com os utilizadores (registo, perfil, etc.).
* **`core/`**: O coração da configuração e segurança.
  * `auth.py` / `security.py`: Lógica de autenticação, validação de tokens e hashing.
  * `configs.py`: Variáveis de ambiente e configurações globais.
  * `database.py`: Configuração da ligação à base de dados.
  * `deps.py`: Injeção de dependências (ex: obter a sessão da base de dados, obter o utilizador atual).
* **`models/`**: Representação das tabelas da base de dados (ex: `artigo_model.py`, `usuario_model.py`).
* **`schemas/`**: Modelos Pydantic para validação de dados de entrada e saída (ex: `artigo_schema.py`, `usuario_schema.py`).
* **`main.py`**: Ponto de entrada principal da aplicação.
* **`criar_tabelas.py`**: Script utilitário para a criação das tabelas na base de dados.

---

## 🗄️ Base de Dados

A API interage com a base de dados de forma assíncrona utilizando um ORM (Object-Relational Mapping). 

* **Modelos Principais**:
  * **Utilizador (`usuario_model`)**: Armazena os dados dos utilizadores, incluindo credenciais de forma segura.
  * **Artigo (`artigo_model`)**: Armazena as publicações, relacionadas de forma relacional ao utilizador que as criou (1:N).
* **Inicialização**: A base de dados não precisa de ser criada manualmente por scripts SQL. Basta executar o ficheiro `criar_tabelas.py` para gerar todo o esquema necessário automaticamente.

---

## 🔐 Criptografia e Segurança

A segurança é um pilar fundamental desta API, implementada no módulo `core`:

* **Hashing de Palavras-passe**: Nenhuma palavra-passe é guardada em texto limpo. Utilizamos algoritmos fortes de criptografia unidirecional (hashing) através do `security.py` para proteger as credenciais dos utilizadores na base de dados.
* **Autenticação via JWT (JSON Web Tokens)**: A autenticação é stateless. Após um login com sucesso, a API emite um token JWT que deve ser enviado no cabeçalho (*Header*) `Authorization: Bearer <token>` nas requisições subsequentes.
* **Proteção de Rotas**: As injeções de dependência (`deps.py`) garantem que endpoints sensíveis (como criar, editar ou apagar artigos) apenas possam ser acedidos por utilizadores devidamente autenticados e autorizados.

---

## 🚀 Forma de Uso

### Pré-requisitos
* Python 3.8+
* Ambiente Virtual (Venv) ativado.

### 1. Instalação das Dependências
Após clonar o repositório e ativar o seu ambiente virtual, instale as bibliotecas necessárias:
```bash
pip install -r requirements.txt
