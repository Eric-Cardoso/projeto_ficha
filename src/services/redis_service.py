from core.configuracoes import cache
from models.ficha_model import Ficha
import json

async def buscar_ficha(id_ficha: int) -> str | None:
    # Tenta obter os dados da ficha no cache
    cache_ficha = await cache.get(f'{id_ficha}')

    return cache_ficha

def obter_ficha(cache_ficha: str) -> dict:
    # Obtém os dados da ficha em forma de dict
    dict_ficha = json.loads(cache_ficha)

    return dict_ficha

async def atualizar_cache(ficha: Ficha, dados_ficha: dict) -> None:
    # Salva os dados da ficha no cache
    await cache.set(f'{ficha.id}', json.dumps(dados_ficha), ex=300)
    

