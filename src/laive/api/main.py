from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from laive.database.config import get_db
from laive.models.periodo import Periodo

app = FastAPI(title="Laive API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "¡Hola desde Laive API!"}

@app.get("/periodos", response_model=List[dict])
async def get_all_periodos(db: AsyncSession = Depends(get_db)):
    """
    Obtiene todos los períodos de la base de datos.
    
    Returns:
        List[dict]: Lista de todos los períodos con sus datos
    """
    # Usar select() en lugar de query() para SQLAlchemy asíncrono
    stmt = select(Periodo)
    result = await db.execute(stmt)
    periodos = result.scalars().all()
    
    # Convertir a diccionarios para la respuesta JSON
    return [
        {
            "periodo": p.periodo,
            "dias_mes": p.dias_mes,
            "dias_mes_ico": p.dias_mes_ico
        }
        for p in periodos
    ] 