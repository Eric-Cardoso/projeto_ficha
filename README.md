# 🧾 Projeto Fichas API

## Descrição

API REST desenvolvida com FastAPI para gerenciamento de usuários e fichas, utilizando autenticação JWT, cache com Redis e ORM com SQLAlchemy.

O sistema possui controle de permissões entre usuários comuns e administradores, permitindo gerenciamento seguro de contas e fichas.

---

# Instruções de instalação

```bash
# Clonar o repositório
git clone https://github.com/Eric-Cardoso/projeto_ficha.git

# Acessar a pasta do projeto
cd projeto_ficha

# Configurar variáveis de ambiente
cp .env-example .env

# preencher o .env com suas configurações

# Criar o ambiente virtual

# Linux / WSL / macOS
python3 -m venv venv

# Windows (PowerShell / CMD)
python -m venv venv

# ou
py -m venv venv

# Ativar o ambiente virtual

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate

# Linux / WSL / macOS
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

---

# Instruções de uso

```bash
# Acessar a pasta src
cd src

# Aplicar migrations
alembic upgrade head

# Iniciar Redis
redis-server

# Rodar a aplicação
fastapi dev app.py
```

Acesse a documentação interativa no navegador:

```txt
http://127.0.0.1:8000/docs
```

Faça login pelo Swagger e utilize as rotas protegidas normalmente.

---

# 📖 Documentação (MkDocs)

Certifique-se de ter instalado as dependências com:

```bash
pip install -r requirements.txt
```

Rodar a documentação localmente

```bash
mkdocs serve -a 127.0.0.1:8001
```

Acesse a documentação no navegador:

```txt
http://127.0.0.1:8001
```