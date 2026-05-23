# 📚 Principais rotas

## Usuários

```txt
POST    /usuarios/criar
GET     /usuarios/me
PATCH   /usuarios/me
DELETE  /usuarios/me
```

## Auth

```txt
POST    /auth/login
GET     /auth/refresh
```

## Fichas

```txt
POST    /fichas/criar
GET     /fichas/listar
GET     /fichas/{id_ficha}
PUT     /fichas/{id_ficha}
PATCH   /fichas/{id_ficha}
DELETE  /fichas/{id_ficha}
```

## Admin

```txt
GET     /admin/usuarios
GET     /admin/usuarios/{id_usuario}
PATCH   /admin/usuarios/{id_usuario}
DELETE  /admin/usuarios/{id_usuario}
GET     /admin/usuarios/{id_usuario}/fichas
GET     /admin/usuarios/{id_usuario}/fichas/{id_ficha}
```

---