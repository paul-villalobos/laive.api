from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from laive.database.config import get_db
from laive.models.periodo import Periodo

app = FastAPI(title="Laive API", version="1.0.0")

@app.get("/")
async def root():
    return {"message": "¡Hola desde Laive API!"}

@app.get("/periodos", response_model=List[dict])
async def get_all_periodos(db: Session = Depends(get_db)):
    """
    Obtiene todos los períodos de la base de datos.
    
    Returns:
        List[dict]: Lista de todos los períodos con sus datos
    """
    periodos = db.query(Periodo).all()
    
    # Convertir a diccionarios para la respuesta JSON
    return [
        {
            "periodo": p.periodo,
            "dias_mes": p.dias_mes,
            "dias_mes_ico": p.dias_mes_ico
        }
        for p in periodos
    ] 