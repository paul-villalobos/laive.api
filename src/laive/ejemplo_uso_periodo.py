#!/usr/bin/env python3
"""
Ejemplo de uso del modelo Periodo.
"""

import sys
import os
import asyncio

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from laive.database.config import AsyncSessionLocal, create_tables
from laive.models.periodo import Periodo
from sqlalchemy import select, func

async def ejemplo_crear_periodos():
    """
    Ejemplo: Crear períodos en la base de datos.
    """
    print("📝 CREANDO PERÍODOS")
    print("=" * 40)
    
    async with AsyncSessionLocal() as db:
        try:
            # Crear períodos de ejemplo
            periodos_a_crear = [
                Periodo(periodo=2023, dias_mes=30, dias_mes_ico=31),
                Periodo(periodo=2024, dias_mes=31, dias_mes_ico=30),
                Periodo(periodo=2025, dias_mes=28, dias_mes_ico=29),
            ]
            
            for periodo in periodos_a_crear:
                db.add(periodo)
                print(f"   Agregando: {periodo}")
            
            await db.commit()
            print(f"✅ {len(periodos_a_crear)} períodos creados exitosamente")
            
        except Exception as e:
            print(f"❌ Error al crear períodos: {e}")
            await db.rollback()

async def ejemplo_consultar_periodos():
    """
    Ejemplo: Consultar períodos de diferentes maneras.
    """
    print("\n📊 CONSULTANDO PERÍODOS")
    print("=" * 40)
    
    async with AsyncSessionLocal() as db:
        try:
            # 1. Obtener todos los períodos
            print("1️⃣ Todos los períodos:")
            stmt = select(Periodo)
            result = await db.execute(stmt)
            todos_periodos = result.scalars().all()
            for p in todos_periodos:
                print(f"   {p}")
            
            # 2. Obtener período específico
            print("\n2️⃣ Período específico (2024):")
            stmt = select(Periodo).where(Periodo.periodo == 2024)
            result = await db.execute(stmt)
            periodo_2024 = result.scalar_one_or_none()
            if periodo_2024:
                print(f"   Encontrado: {periodo_2024}")
            else:
                print("   ❌ Período 2024 no encontrado")
            
            # 3. Filtrar períodos
            print("\n3️⃣ Períodos con más de 30 días:")
            stmt = select(Periodo).where(Periodo.dias_mes > 30)
            result = await db.execute(stmt)
            periodos_largos = result.scalars().all()
            for p in periodos_largos:
                print(f"   {p}")
            
            # 4. Contar períodos
            stmt = select(func.count(Periodo.periodo))
            result = await db.execute(stmt)
            total_periodos = result.scalar()
            print(f"\n4️⃣ Total de períodos en la base de datos: {total_periodos}")
            
        except Exception as e:
            print(f"❌ Error al consultar: {e}")

async def ejemplo_actualizar_periodo():
    """
    Ejemplo: Actualizar un período existente.
    """
    print("\n✏️ ACTUALIZANDO PERÍODO")
    print("=" * 40)
    
    async with AsyncSessionLocal() as db:
        try:
            # Buscar período 2024
            stmt = select(Periodo).where(Periodo.periodo == 2024)
            result = await db.execute(stmt)
            periodo = result.scalar_one_or_none()
            
            if periodo:
                print(f"   Período antes: {periodo}")
                
                # Actualizar valores
                periodo.dias_mes = 32
                periodo.dias_mes_ico = 33
                
                await db.commit()
                print(f"   Período después: {periodo}")
                print("   ✅ Período actualizado exitosamente")
            else:
                print("   ❌ Período 2024 no encontrado")
                
        except Exception as e:
            print(f"❌ Error al actualizar: {e}")
            await db.rollback()

async def ejemplo_eliminar_periodo():
    """
    Ejemplo: Eliminar un período.
    """
    print("\n🗑️ ELIMINANDO PERÍODO")
    print("=" * 40)
    
    async with AsyncSessionLocal() as db:
        try:
            # Buscar período 2025
            stmt = select(Periodo).where(Periodo.periodo == 2025)
            result = await db.execute(stmt)
            periodo = result.scalar_one_or_none()
            
            if periodo:
                print(f"   Eliminando: {periodo}")
                await db.delete(periodo)
                await db.commit()
                print("   ✅ Período eliminado exitosamente")
            else:
                print("   ❌ Período 2025 no encontrado")
                
        except Exception as e:
            print(f"❌ Error al eliminar: {e}")
            await db.rollback()

async def ejemplo_operaciones_avanzadas():
    """
    Ejemplo: Operaciones más avanzadas.
    """
    print("\n🔬 OPERACIONES AVANZADAS")
    print("=" * 40)
    
    async with AsyncSessionLocal() as db:
        try:
            # 1. Ordenar períodos
            print("1️⃣ Períodos ordenados por año:")
            stmt = select(Periodo).order_by(Periodo.periodo.desc())
            result = await db.execute(stmt)
            periodos_ordenados = result.scalars().all()
            for p in periodos_ordenados:
                print(f"   {p}")
            
            # 2. Límite de resultados
            print("\n2️⃣ Últimos 2 períodos:")
            stmt = select(Periodo).order_by(Periodo.periodo.desc()).limit(2)
            result = await db.execute(stmt)
            ultimos_periodos = result.scalars().all()
            for p in ultimos_periodos:
                print(f"   {p}")
            
            # 3. Estadísticas
            print("\n3️⃣ Estadísticas:")
            stmt = select(func.count(Periodo.periodo))
            result = await db.execute(stmt)
            total = result.scalar()
            
            stmt = select(Periodo.dias_mes).where(Periodo.dias_mes.isnot(None))
            result = await db.execute(stmt)
            promedio_dias = result.scalars().all()
            if promedio_dias:
                promedio = sum(promedio_dias) / len(promedio_dias)
                print(f"   Total períodos: {total}")
                print(f"   Promedio días: {promedio:.1f}")
            
        except Exception as e:
            print(f"❌ Error en operaciones avanzadas: {e}")

async def main():
    """
    Ejecutar todos los ejemplos.
    """
    print("🎯 EJEMPLOS DE USO DEL MODELO PERIODO")
    print("=" * 50)
    
    # Crear tablas si no existen
    try:
        await create_tables()
        print("✅ Tablas creadas/verificadas")
    except Exception as e:
        print(f"❌ Error al crear tablas: {e}")
        return
    
    # Ejecutar ejemplos
    await ejemplo_crear_periodos()
    await ejemplo_consultar_periodos()
    await ejemplo_actualizar_periodo()
    await ejemplo_eliminar_periodo()
    await ejemplo_operaciones_avanzadas()
    
    print("\n🎉 ¡Todos los ejemplos completados!")

if __name__ == "__main__":
    asyncio.run(main()) 