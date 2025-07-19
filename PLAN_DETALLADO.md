# 📋 PLAN DETALLADO - Laive API

## 🎯 Objetivo del Proyecto

Construir una API REST robusta usando **Python 3.13, FastAPI, SQLAlchemy 2, PostgreSQL** y contenedores **Docker Compose** administrados con **Poetry**.

---

## 🏗️ Arquitectura del Sistema

### **Stack Tecnológico**

- **Backend**: Python 3.13 + FastAPI
- **ORM**: SQLAlchemy 2.0
- **Base de Datos**: PostgreSQL
- **Contenedores**: Docker + Docker Compose
- **Gestión de Dependencias**: Poetry
- **Sistema Operativo**: Windows

### **Estructura del Proyecto**

```
laive.api/
├── 📁 src/laive/
│   ├── 📁 api/           # Endpoints FastAPI
│   ├── 📁 models/        # Modelos SQLAlchemy
│   ├── 📁 schemas/       # Esquemas Pydantic
│   ├── 📁 database/      # Configuración DB
│   ├── 📁 services/      # Lógica de negocio
│   └── 📁 utils/         # Utilidades
├── 📁 tests/             # Tests unitarios
├── 📁 scripts/           # Scripts de utilidad
├── 📁 alembic/           # Migraciones
├── 📄 pyproject.toml     # Configuración Poetry
├── 📄 docker-compose.yml # Contenedores
└── 📄 .env.example       # Variables de entorno
```

---

## 📅 Fases de Desarrollo

### **FASE 1: Configuración Base** ✅

- [x] Estructura del proyecto
- [x] Configuración Poetry
- [x] Sistema de entornos (.env)
- [x] Archivo de prueba básico
- [x] .gitignore configurado

### **FASE 2: Dependencias y Configuración**

- [ ] Instalar dependencias principales

  - [ ] `fastapi` - Framework web
  - [ ] `sqlalchemy` - ORM
  - [ ] `psycopg2-binary` - Driver PostgreSQL
  - [ ] `alembic` - Migraciones
  - [ ] `python-dotenv` - Variables de entorno
  - [ ] `pydantic` - Validación de datos
  - [ ] `uvicorn` - Servidor ASGI

- [ ] Configurar estructura de carpetas
  - [ ] `src/laive/database/` - Configuración DB
  - [ ] `src/laive/models/` - Modelos SQLAlchemy
  - [ ] `src/laive/schemas/` - Esquemas Pydantic
  - [ ] `src/laive/api/` - Endpoints FastAPI
  - [ ] `src/laive/services/` - Lógica de negocio

### **FASE 3: Base de Datos**

- [ ] Configurar conexión PostgreSQL

  - [ ] Engine SQLAlchemy
  - [ ] Session factory
  - [ ] Configuración de pool de conexiones

- [ ] Crear modelos de ejemplo

  - [ ] Modelo `User` (usuarios)
  - [ ] Modelo `Product` (productos)
  - [ ] Relaciones entre modelos

- [ ] Configurar Alembic
  - [ ] Inicializar Alembic
  - [ ] Crear primera migración
  - [ ] Scripts de migración

### **FASE 4: API FastAPI**

- [ ] Configurar aplicación FastAPI

  - [ ] App principal
  - [ ] Middleware CORS
  - [ ] Configuración de logging
  - [ ] Manejo de errores

- [ ] Crear endpoints básicos

  - [ ] Health check (`/health`)
  - [ ] CRUD de usuarios
  - [ ] CRUD de productos
  - [ ] Autenticación básica

- [ ] Implementar validación
  - [ ] Esquemas Pydantic
  - [ ] Validación de entrada
  - [ ] Respuestas tipadas

### **FASE 5: Docker y Contenedores**

- [ ] Configurar Docker

  - [ ] Dockerfile para la aplicación
  - [ ] docker-compose.yml
  - [ ] Contenedor PostgreSQL
  - [ ] Red de contenedores

- [ ] Scripts de Docker
  - [ ] Build de imagen
  - [ ] Ejecución en desarrollo
  - [ ] Ejecución en producción

### **FASE 6: Testing y Calidad**

- [ ] Configurar testing

  - [ ] pytest
  - [ ] Tests unitarios
  - [ ] Tests de integración
  - [ ] Coverage

- [ ] Herramientas de calidad
  - [ ] black (formateo)
  - [ ] flake8 (linting)
  - [ ] mypy (type checking)

### **FASE 7: Documentación y Despliegue**

- [ ] Documentación

  - [ ] README completo
  - [ ] Documentación de API
  - [ ] Guías de desarrollo

- [ ] Scripts de despliegue
  - [ ] Scripts de migración
  - [ ] Scripts de backup
  - [ ] Monitoreo básico

---

## 🔧 Comandos de Desarrollo

### **Gestión de Dependencias**

```bash
# Instalar dependencias
poetry install

# Agregar nueva dependencia
poetry add fastapi sqlalchemy psycopg2-binary

# Agregar dependencia de desarrollo
poetry add --group dev pytest black flake8
```

### **Ejecución de la Aplicación**

```bash
# Desarrollo
poetry run uvicorn src.laive.main:app --reload

# Producción
poetry run uvicorn src.laive.main:app --host 0.0.0.0 --port 8000
```

### **Base de Datos**

```bash
# Inicializar Alembic
alembic init alembic

# Crear migración
alembic revision --autogenerate -m "Initial migration"

# Ejecutar migraciones
alembic upgrade head

# Revertir migración
alembic downgrade -1
```

### **Docker**

```bash
# Construir imagen
docker build -t laive-api .

# Ejecutar con Docker Compose
docker compose up -d

# Ver logs
docker compose logs -f

# Detener servicios
docker compose down
```

### **Testing**

```bash
# Ejecutar tests
poetry run pytest

# Con coverage
poetry run pytest --cov=src

# Formatear código
poetry run black src/

# Linting
poetry run flake8 src/
```

---

## 📊 Estructura de Base de Datos

### **Tabla Users**

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### **Tabla Products**

```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    stock INTEGER DEFAULT 0,
    user_id INTEGER REFERENCES users(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 🚀 Endpoints de la API

### **Health Check**

- `GET /health` - Estado de la aplicación

### **Usuarios**

- `POST /users/` - Crear usuario
- `GET /users/` - Listar usuarios
- `GET /users/{id}` - Obtener usuario
- `PUT /users/{id}` - Actualizar usuario
- `DELETE /users/{id}` - Eliminar usuario

### **Productos**

- `POST /products/` - Crear producto
- `GET /products/` - Listar productos
- `GET /products/{id}` - Obtener producto
- `PUT /products/{id}` - Actualizar producto
- `DELETE /products/{id}` - Eliminar producto

---

## 🔒 Consideraciones de Seguridad

### **Autenticación**

- [ ] JWT tokens
- [ ] Password hashing (bcrypt)
- [ ] Rate limiting
- [ ] CORS configurado

### **Validación**

- [ ] Input validation con Pydantic
- [ ] SQL injection prevention
- [ ] XSS protection
- [ ] CSRF protection

### **Logging**

- [ ] Logs de acceso
- [ ] Logs de errores
- [ ] Logs de seguridad
- [ ] Rotación de logs

---

## 📈 Métricas y Monitoreo

### **Métricas Básicas**

- [ ] Response time
- [ ] Error rate
- [ ] Database connections
- [ ] Memory usage

### **Health Checks**

- [ ] Database connectivity
- [ ] External services
- [ ] Disk space
- [ ] Memory usage

---

## 🎯 Criterios de Éxito

### **Funcionalidad**

- [ ] API completamente funcional
- [ ] CRUD operations implementadas
- [ ] Autenticación funcionando
- [ ] Base de datos configurada

### **Calidad**

- [ ] Tests pasando (>80% coverage)
- [ ] Código formateado y linted
- [ ] Documentación completa
- [ ] Docker funcionando

### **Performance**

- [ ] Response time < 200ms
- [ ] Database queries optimizadas
- [ ] Connection pooling configurado
- [ ] Caching implementado

---

## 📝 Notas de Desarrollo

### **Principios**

1. **KISS** - Keep It Simple, Stupid
2. **YAGNI** - You Aren't Gonna Need It
3. **DRY** - Don't Repeat Yourself
4. **SOLID** - Principios de diseño

### **Convenciones**

- Nombres de archivos en snake_case
- Nombres de clases en PascalCase
- Nombres de variables en snake_case
- Constantes en UPPER_CASE

### **Commits**

- Usar mensajes descriptivos
- Prefijos: feat, fix, docs, style, refactor, test, chore
- Ejemplo: `feat: add user authentication endpoints`

---

## 🔄 Próximos Pasos Inmediatos

1. **Instalar dependencias con Poetry**
2. **Configurar estructura de carpetas**
3. **Implementar configuración de base de datos**
4. **Crear primeros modelos SQLAlchemy**
5. **Configurar Alembic para migraciones**
6. **Implementar endpoints básicos de FastAPI**

---

_Este plan está diseñado para ser iterativo y puede ajustarse según las necesidades específicas del proyecto._
