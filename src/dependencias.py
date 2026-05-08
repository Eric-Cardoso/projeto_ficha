from core.configuracoes import SessionLocal

# Empresta a sessao do banco de dados sempre que necessário
async def sessao():
    async with SessionLocal() as sessao: 
        yield sessao



    