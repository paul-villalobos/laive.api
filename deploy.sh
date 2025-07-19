#!/bin/bash

# Script de despliegue para Laive API
set -e

echo "🚀 Iniciando despliegue de Laive API..."

# Verificar que Docker esté instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado. Por favor instálalo primero."
    exit 1
fi

# Verificar que Docker Compose esté instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose no está instalado. Por favor instálalo primero."
    exit 1
fi

# Construir la imagen
echo "📦 Construyendo imagen Docker..."
docker build -t laive-api:latest .

# Verificar si la construcción fue exitosa
if [ $? -eq 0 ]; then
    echo "✅ Imagen construida exitosamente"
else
    echo "❌ Error al construir la imagen"
    exit 1
fi

# Ejecutar con Docker Compose
echo "🐳 Iniciando servicios con Docker Compose..."
docker-compose up -d

# Esperar un momento para que los servicios se inicien
echo "⏳ Esperando que los servicios se inicien..."
sleep 10

# Verificar el estado de los servicios
echo "🔍 Verificando estado de los servicios..."
docker-compose ps

echo "✅ Despliegue completado!"
echo "🌐 La API estará disponible en: http://localhost:8000"
echo "📊 Documentación de la API: http://localhost:8000/docs"
echo ""
echo "Para ver los logs: docker-compose logs -f"
echo "Para detener: docker-compose down" 