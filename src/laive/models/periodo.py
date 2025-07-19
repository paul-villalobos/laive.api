from sqlalchemy import Column, Integer, SmallInteger
from laive.database.config import Base

class Periodo(Base):
    """
    Modelo para la tabla gpc.periodo.
    
    Representa períodos con información sobre días del mes.
    """
    __tablename__ = "periodo"
    __table_args__ = {"schema": "gpc"}  # Especificar el esquema
    
    # Clave primaria - período (año)
    periodo = Column(Integer, primary_key=True, nullable=False)
    
    # Días del mes (opcional)
    dias_mes = Column(SmallInteger, nullable=True)
    
    # Días del mes ICO (opcional)
    dias_mes_ico = Column(SmallInteger, nullable=True)
    
    def __repr__(self):
        return f"<Periodo(periodo={self.periodo}, dias_mes={self.dias_mes}, dias_mes_ico={self.dias_mes_ico})>"
    
    def __str__(self):
        return f"Período {self.periodo} - Días: {self.dias_mes}, Días ICO: {self.dias_mes_ico}" 