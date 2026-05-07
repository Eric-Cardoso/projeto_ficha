from fastapi import FastAPI, status

# Configura o app
app = FastAPI(title='projeto-ficha', version='0.1.0')

@app.get(path='/', status_code=status.HTTP_200_OK)
async def home():
    return {
        'status': 'ok'    
    }