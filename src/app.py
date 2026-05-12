from fastapi import FastAPI, status
from routers import usuario_rota

# Configura o app
app = FastAPI(title='projeto-ficha', version='0.1.0')

# Inclui as rotas no app
app.include_router(usuario_rota.usuario_rota)

@app.get(path='/', status_code=status.HTTP_200_OK)
async def home():
    return {
        'status': 'ok'    
    }