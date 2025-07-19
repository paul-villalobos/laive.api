# Laive API

API REST con FastAPI, SQLAlchemy 2 y PostgreSQL.

## 🚀 Desarrollo

### Instalar dependencias

```bash
poetry install
```

### Configurar variables de entorno

#### Opción 1: Usar el script automático

```bash
python setup_env.py
```

#### Opción 2: Configurar manualmente

1. Copia el archivo de ejemplo:

```bash
cp env.example .env
```

2. Edita `.env` con tus valores:

```bash
# Base de datos
DATABASE_URL=postgresql://postgres:password@localhost:5432/laive_db

# Seguridad
SECRET_KEY=tu-clave-secreta-super-segura

# Entorno
ENVIRONMENT=development
DEBUG=true
LOG_LEVEL=debug
```

### Ejecutar en desarrollo

```bash
poetry run uvicorn src.laive.api.main:app --reload
```

## 🐳 Docker

### Desarrollo local

```bash
docker-compose up --build
```

### Producción

```bash
docker build -t laive-api .
docker run -p 8000:8000 laive-api
```

## 🌐 Despliegue en EasyPanel

### 1. Configurar variables de entorno en EasyPanel

Ve a tu proyecto en EasyPanel → Environment Variables y agrega:

```
DATABASE_URL=postgresql://postgres:tu_password@tu_host:5432/tu_db
SECRET_KEY=tu-clave-secreta-super-segura
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=info
PORT=8000
HOST=0.0.0.0
ALLOWED_ORIGINS=https://tu-dominio.com
RATE_LIMIT_PER_MINUTE=100
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20
DB_POOL_TIMEOUT=30
```

### 2. Desplegar

1. Sube tu código al repositorio
2. Conecta el repositorio en EasyPanel
3. EasyPanel leerá automáticamente `easypanel.yml`
4. Despliega

## 📚 Documentación

- **API Docs:** `http://localhost:8000/docs`
- **Health Check:** `http://localhost:8000/`
- **Períodos:** `http://localhost:8000/periodos`

## 🔧 Variables de Entorno

| Variable                | Descripción                   | Valor por defecto                                        |
| ----------------------- | ----------------------------- | -------------------------------------------------------- |
| `DATABASE_URL`          | URL de conexión PostgreSQL    | `postgresql://postgres:password@localhost:5432/laive_db` |
| `SECRET_KEY`            | Clave secreta para JWT        | `dev-secret-key-change-in-production`                    |
| `ENVIRONMENT`           | Entorno (dev/staging/prod)    | `development`                                            |
| `DEBUG`                 | Modo debug                    | `true`                                                   |
| `LOG_LEVEL`             | Nivel de logging              | `debug`                                                  |
| `PORT`                  | Puerto de la aplicación       | `8000`                                                   |
| `HOST`                  | Host de la aplicación         | `0.0.0.0`                                                |
| `ALLOWED_ORIGINS`       | Orígenes CORS permitidos      | `http://localhost:3000,http://localhost:8080`            |
| `RATE_LIMIT_PER_MINUTE` | Límite de requests/min        | `100`                                                    |
| `DB_POOL_SIZE`          | Tamaño del pool de conexiones | `10`                                                     |
| `DB_MAX_OVERFLOW`       | Overflow máximo del pool      | `20`                                                     |
| `DB_POOL_TIMEOUT`       | Timeout del pool (segundos)   | `30`                                                     |
