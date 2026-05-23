# 🔐 Autenticação

A autenticação é feita utilizando JWT.

## Fluxo:

- usuário envia email e senha
- sistema valida credenciais
- retorna:
  - access_token
  - refresh_token
- rotas protegidas exigem usuário autenticado

Senhas são armazenadas de forma segura utilizando hash com Bcrypt.

---