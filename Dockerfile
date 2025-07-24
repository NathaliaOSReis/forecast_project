FROM python:3.10-slim

WORKDIR /app

# Instalar curl para healthcheck
RUN apt-get update && apt-get install -y curl && apt-get clean

# Copiar arquivos de requisitos e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --no-cache-dir uvicorn streamlit

# Copiar o restante dos arquivos do projeto
COPY . .

# Definir variáveis de ambiente padrão
ENV PYTHONUNBUFFERED=1

# O comando será sobrescrito no docker-compose para cada serviço
CMD ["python", "-c", "print('Especifique um comando no docker-compose.yml')"]



