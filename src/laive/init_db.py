#!/usr/bin/env python3
"""
Script para verificar la conectividad con la base de datos.
Solo verifica que la conexión esté disponible.
"""

import os
import sys
import time
import asyncio
from sqlalchemy import text

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from laive.database.config import engine

async def wait_for_db():
    """Esperar a que la base de datos esté disponible."""
    max_attempts = 30
    attempt = 0
    
    while attempt < max_attempts:
        try:
            async with engine.connect() as conn:
                await conn.execute(text("SELECT 1"))
                print("✅ Base de datos conectada exitosamente")
                return True
        except Exception as e:
            attempt += 1
            print(f"⏳ Intento {attempt}/{max_attempts}: Esperando conexión a la base de datos...")
            await asyncio.sleep(2)
    
    print("❌ No se pudo conectar a la base de datos después de 60 segundos")
    return False

async def check_database_connection():
    """Verificar la conectividad con la base de datos."""
    print("🔍 Verificando conectividad con la base de datos...")
    
    # Esperar a que la base de datos esté disponible
    if not await wait_for_db():
        print("❌ No se pudo establecer conexión con la base de datos")
        sys.exit(1)
    
    try:
        # Verificar que podemos ejecutar consultas
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT version()"))
            version = result.fetchone()[0]
            print(f"✅ Conexión exitosa a PostgreSQL: {version}")
        
        print("✅ Conectividad con la base de datos verificada correctamente")
        
    except Exception as e:
        print(f"❌ Error al verificar la base de datos: {e}")
        sys.exit(1)

async def main():
    """Función principal asíncrona."""
    await check_database_connection()

if __name__ == "__main__":
    asyncio.run(main()) 