# Usar Python 3.13 slim
FROM python:3.13-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias para psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivos de configuración de Poetry
COPY pyproject.toml poetry.lock ./

# Instalar Poetry
RUN pip install poetry

# Configurar Poetry para no crear entorno virtual
RUN poetry config virtualenvs.create false

# Copiar código fuente ANTES de instalar dependencias
COPY src/ ./src/

# Instalar dependencias DESPUÉS de copiar el código
RUN poetry install --only=main

# Establecer PYTHONPATH para incluir src
ENV PYTHONPATH=/app/src:$PYTHONPATH

# Exponer puerto
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["poetry", "run", "uvicorn", "laive.api.main:app", "--host", "0.0.0.0", "--port", "8000"] 