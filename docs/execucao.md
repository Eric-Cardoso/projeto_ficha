# ⚙️ Execução do projeto

```bash
# Acessar a pasta src
cd src

# Rodar as migrations
alembic upgrade head

# Iniciar Redis
redis-server

# Iniciar o servidor
fastapi dev app.py
```

Acesse a documentação interativa no navegador:

```txt
http://127.0.0.1:8000/docs
```

Faça login pelo Swagger e utilize as rotas protegidas normalmente.

---