from fastapi import FastAPI, status
from routers import usuario_rotas, auth_rotas, ficha_rotas, admin_rotas

# Configura o app
app = FastAPI(title='projeto-ficha', version='0.1.0')

# Inclui as rotas no app
app.include_router(usuario_rotas.usuario_rota)
app.include_router(auth_rotas.auth_rota)
app.include_router(ficha_rotas.ficha_rota)
app.include_router(admin_rotas.admin_rota)

@app.get(path='/', status_code=status.HTTP_200_OK)
async def home():
    return {
        'status': 'ok'    
    }