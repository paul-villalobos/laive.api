#!/usr/bin/env python3
"""
Ejemplo de uso del modelo Periodo.
"""

import sys
import os

# Agregar el directorio src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from laive.database.config import SessionLocal, create_tables
from laive.models.periodo import Periodo

def ejemplo_crear_periodos():
    """
    Ejemplo: Crear períodos en la base de datos.
    """
    print("📝 CREANDO PERÍODOS")
    print("=" * 40)
    
    db = SessionLocal()
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
        
        db.commit()
        print(f"✅ {len(periodos_a_crear)} períodos creados exitosamente")
        
    except Exception as e:
        print(f"❌ Error al crear períodos: {e}")
        db.rollback()
    finally:
        db.close()

def ejemplo_consultar_periodos():
    """
    Ejemplo: Consultar períodos de diferentes maneras.
    """
    print("\n📊 CONSULTANDO PERÍODOS")
    print("=" * 40)
    
    db = SessionLocal()
    try:
        # 1. Obtener todos los períodos
        print("1️⃣ Todos los períodos:")
        todos_periodos = db.query(Periodo).all()
        for p in todos_periodos:
            print(f"   {p}")
        
        # 2. Obtener período específico
        print("\n2️⃣ Período específico (2024):")
        periodo_2024 = db.query(Periodo).filter(Periodo.periodo == 2024).first()
        if periodo_2024:
            print(f"   Encontrado: {periodo_2024}")
        else:
            print("   ❌ Período 2024 no encontrado")
        
        # 3. Filtrar períodos
        print("\n3️⃣ Períodos con más de 30 días:")
        periodos_largos = db.query(Periodo).filter(Periodo.dias_mes > 30).all()
        for p in periodos_largos:
            print(f"   {p}")
        
        # 4. Contar períodos
        total_periodos = db.query(Periodo).count()
        print(f"\n4️⃣ Total de períodos en la base de datos: {total_periodos}")
        
    except Exception as e:
        print(f"❌ Error al consultar: {e}")
    finally:
        db.close()

def ejemplo_actualizar_periodo():
    """
    Ejemplo: Actualizar un período existente.
    """
    print("\n✏️ ACTUALIZANDO PERÍODO")
    print("=" * 40)
    
    db = SessionLocal()
    try:
        # Buscar período 2024
        periodo = db.query(Periodo).filter(Periodo.periodo == 2024).first()
        
        if periodo:
            print(f"   Período antes: {periodo}")
            
            # Actualizar valores
            periodo.dias_mes = 32
            periodo.dias_mes_ico = 33
            
            db.commit()
            print(f"   Período después: {periodo}")
            print("   ✅ Período actualizado exitosamente")
        else:
            print("   ❌ Período 2024 no encontrado")
            
    except Exception as e:
        print(f"❌ Error al actualizar: {e}")
        db.rollback()
    finally:
        db.close()

def ejemplo_eliminar_periodo():
    """
    Ejemplo: Eliminar un período.
    """
    print("\n🗑️ ELIMINANDO PERÍODO")
    print("=" * 40)
    
    db = SessionLocal()
    try:
        # Buscar período 2025
        periodo = db.query(Periodo).filter(Periodo.periodo == 2025).first()
        
        if periodo:
            print(f"   Eliminando: {periodo}")
            db.delete(periodo)
            db.commit()
            print("   ✅ Período eliminado exitosamente")
        else:
            print("   ❌ Período 2025 no encontrado")
            
    except Exception as e:
        print(f"❌ Error al eliminar: {e}")
        db.rollback()
    finally:
        db.close()

def ejemplo_operaciones_avanzadas():
    """
    Ejemplo: Operaciones más avanzadas.
    """
    print("\n🔬 OPERACIONES AVANZADAS")
    print("=" * 40)
    
    db = SessionLocal()
    try:
        # 1. Ordenar períodos
        print("1️⃣ Períodos ordenados por año:")
        periodos_ordenados = db.query(Periodo).order_by(Periodo.periodo.desc()).all()
        for p in periodos_ordenados:
            print(f"   {p}")
        
        # 2. Límite de resultados
        print("\n2️⃣ Últimos 2 períodos:")
        ultimos_periodos = db.query(Periodo).order_by(Periodo.periodo.desc()).limit(2).all()
        for p in ultimos_periodos:
            print(f"   {p}")
        
        # 3. Estadísticas
        print("\n3️⃣ Estadísticas:")
        total = db.query(Periodo).count()
        promedio_dias = db.query(Periodo.dias_mes).filter(Periodo.dias_mes.isnot(None)).all()
        if promedio_dias:
            promedio = sum(d[0] for d in promedio_dias) / len(promedio_dias)
            print(f"   Total períodos: {total}")
            print(f"   Promedio días: {promedio:.1f}")
        
    except Exception as e:
        print(f"❌ Error en operaciones avanzadas: {e}")
    finally:
        db.close()

def main():
    """
    Ejecutar todos los ejemplos.
    """
    print("🎯 EJEMPLOS DE USO DEL MODELO PERIODO")
    print("=" * 50)
    
    # Crear tablas si no existen
    try:
        create_tables()
        print("✅ Tablas creadas/verificadas")
    except Exception as e:
        print(f"❌ Error al crear tablas: {e}")
        return
    
    # Ejecutar ejemplos
    ejemplo_crear_periodos()
    ejemplo_consultar_periodos()
    ejemplo_actualizar_periodo()
    ejemplo_eliminar_periodo()
    ejemplo_operaciones_avanzadas()
    
    print("\n🎉 ¡Todos los ejemplos completados!")

if __name__ == "__main__":
    main() 