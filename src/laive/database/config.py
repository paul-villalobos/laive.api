import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Obtener variables de entorno con valores por defecto
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/laive_db")
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-in-production")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "debug")

# Configuración de pool de conexiones
DB_POOL_SIZE = int(os.getenv("DB_POOL_SIZE", "10"))
DB_MAX_OVERFLOW = int(os.getenv("DB_MAX_OVERFLOW", "20"))
DB_POOL_TIMEOUT = int(os.getenv("DB_POOL_TIMEOUT", "30"))

# Convertir URL síncrona a asíncrona si es necesario
if DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

# Crear el engine asíncrono de SQLAlchemy con configuración optimizada
engine = create_async_engine(
    DATABASE_URL,
    echo=DEBUG,  # Mostrar SQL en consola solo en desarrollo
    pool_pre_ping=True,  # Verificar conexiones antes de usar
    pool_recycle=300,  # Reciclar conexiones cada 5 minutos
    pool_size=DB_POOL_SIZE,
    max_overflow=DB_MAX_OVERFLOW,
    pool_timeout=DB_POOL_TIMEOUT,
)

# Crear la sesión asíncrona de base de datos
AsyncSessionLocal = async_sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# Crear la base para los modelos
Base = declarative_base()

# Función para obtener la sesión de base de datos asíncrona
async def get_db():
    """
    Función para obtener una sesión de base de datos asíncrona.
    Se usa como dependencia en FastAPI.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()

# Función para crear todas las tablas
async def create_tables():
    """
    Crear todas las tablas definidas en los modelos.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)