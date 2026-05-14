from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from password_strength import PasswordPolicy
from datetime import timedelta, datetime, timezone
from jose import jwt
from core.configuracoes import CHAVE_SECRETA, ALGORITMO, TEMPO_EXPIRACAO_TOKEN

# Configura o bcrypt
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# Configura o oauth2
oauth2_schema = OAuth2PasswordBearer(tokenUrl='auth/login')

def validar_senha(senha: str) -> None:
    # Determina os requisitos para a senha ser válida
    policy = PasswordPolicy.from_names(
        length=8, uppercase=1, numbers=1, special=1
    )

    # Coleta os erros que a senha possa ter
    erros = policy.test(password=senha)

    # Verifica se algum erro foi encontrado
    if erros:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT, 
            detail={
                'mensagem': 'Senha inválida',
                'requisitos': [
                    'minimo 8 caracteres',
                    '1 letra maiúscula',
                    '1 número',
                    '1 caractere especial',
                ]
            }
        )
    
def gerar_token(
    id_usuario, 
    tempo_expiracao_token: timedelta = timedelta(minutes=TEMPO_EXPIRACAO_TOKEN)
) -> str:
    
    # Define a data de expiração do token
    data_expiracao_token = datetime.now(timezone.utc) + tempo_expiracao_token
    
    # Contém as informações que irão no token
    dict_info = {
        'sub': str(id_usuario),
        'exp': data_expiracao_token
    }

    # Cria o token
    token = jwt.encode(claims=dict_info, key=CHAVE_SECRETA, algorithm=ALGORITMO)

    return token
    