# Usar Python 3.13 slim
FROM python:3.13-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de configuración
COPY pyproject.toml poetry.lock ./

# Copiar código fuente ANTES de instalar dependencias
COPY src/ ./src/

# Instalar Poetry
RUN pip install poetry

# Configurar Poetry para no crear entorno virtual
RUN poetry config virtualenvs.create false

# Instalar dependencias (ahora Poetry puede encontrar el paquete laive)
RUN poetry install --only=main

# Establecer PYTHONPATH para incluir src
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Exponer puerto
EXPOSE 8000

# Script de inicialización
COPY src/laive/init_db.py ./src/laive/

# Comando para ejecutar la aplicación
CMD ["sh", "-c", "poetry run python src/laive/init_db.py && poetry run uvicorn laive.api.main:app --host 0.0.0.0 --port 8000"] 