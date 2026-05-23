# 📦 Instalação

```bash
# Clonar o repositório
git clone https://github.com/Eric-Cardoso/projeto_ficha.git

# Acessar a pasta do projeto
cd projeto_ficha

# Configurar variáveis de ambiente
cp .env-example .env

# preencher o .env com suas configurações

# Criar o ambiente virtual

# Linux / WSL / macOS
python3 -m venv venv

# Windows (PowerShell / CMD)
python -m venv venv

# ou
py -m venv venv

# Ativar o ambiente virtual

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (CMD)
venv\Scripts\activate

# Linux / WSL / macOS
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

---