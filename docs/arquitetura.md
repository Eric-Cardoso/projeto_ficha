# 🧱 Arquitetura do projeto

O projeto está organizado em camadas:

- routes → definição das rotas
- services → regras de negócio
- repos → acesso ao banco de dados
- schemas → validação de dados (Pydantic)
- models → estrutura das tabelas (SQLAlchemy)
- core → configurações e segurança
- services → cache e serviços auxiliares

---