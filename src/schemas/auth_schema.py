from pydantic import BaseModel

class TokenPublico(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str