from fastapi import HTTPException, status
from passlib.context import CryptContext
from password_strength import PasswordPolicy

# Configura o bcrypt
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def validar_senha(senha: str) -> None:
    # Determinar os requisitos para a senha ser válida
    policy = PasswordPolicy.from_names(
        length=8, uppercase=1, numbers=1, special=1
    )

    # Coleta os erros que senha possa ter
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
    