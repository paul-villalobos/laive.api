# 🚀 Guía de Despliegue en EasyPanel

Esta guía te ayudará a desplegar tu aplicación Laive API en EasyPanel paso a paso.

## 📋 Prerrequisitos

- ✅ Cuenta en EasyPanel
- ✅ Repositorio Git (GitHub, GitLab, etc.)
- ✅ Código subido al repositorio
- ✅ Base de datos PostgreSQL existente en EasyPanel

---

## 🔧 Paso 1: Preparar el Repositorio

### 1.1 Verificar archivos necesarios

Asegúrate de que tu repositorio contenga estos archivos:

```
laive.api/
├── Dockerfile              ✅
├── docker-compose.yml      ✅
├── easypanel.yml          ✅
├── pyproject.toml         ✅
├── src/                   ✅
├── README.md              ✅
└── .gitignore             ✅
```

### 1.2 Subir cambios al repositorio

```bash
git add .
git commit -m "Preparar para despliegue en EasyPanel con variables de entorno"
git push origin main
```

---

## 🌐 Paso 2: Configurar EasyPanel

### 2.1 Crear nuevo proyecto

1. Inicia sesión en [EasyPanel](https://easypanel.io)
2. Haz clic en **"New Project"**
3. Selecciona **"From Git Repository"**

### 2.2 Conectar repositorio

1. Selecciona tu proveedor Git (GitHub, GitLab, etc.)
2. Autoriza EasyPanel para acceder a tu repositorio
3. Selecciona el repositorio `laive.api`
4. Selecciona la rama `main`

---

## ⚙️ Paso 3: Configurar Variables de Entorno

### 3.1 Obtener datos de la base de datos existente

1. **En EasyPanel, ve a tu base de datos PostgreSQL existente**
2. **Copia los datos de conexión:**

   - Host: `tu_host_postgres`
   - Puerto: `5432` (por defecto)
   - Usuario: `postgres` (por defecto)
   - Contraseña: `tu_password`
   - Base de datos: `tu_nombre_db`

### 3.2 Configurar variables en EasyPanel

1. Ve a tu proyecto en EasyPanel
2. Ve a la sección **"Environment Variables"**
3. Agrega las siguientes variables:

```bash
# ===== CONFIGURACIÓN DE BASE DE DATOS =====
DATABASE_URL=postgresql://postgres:tu_password@tu_host_postgres:5432/tu_nombre_db

# ===== CONFIGURACIÓN DE SEGURIDAD =====
SECRET_KEY=tu-clave-secreta-super-segura-cambiar-en-produccion

# ===== CONFIGURACIÓN DE ENTORNO =====
ENVIRONMENT=production
DEBUG=false
LOG_LEVEL=info

# ===== CONFIGURACIÓN DE POOL DE BASE DE DATOS (OPCIONAL) =====
DB_POOL_SIZE=10
DB_MAX_OVERFLOW=20
DB_POOL_TIMEOUT=30
```

**⚠️ IMPORTANTE:** Reemplaza los valores con tus datos reales:

- `tu_password`: Contraseña real de tu base de datos
- `tu_host_postgres`: Host real de tu base de datos
- `tu_nombre_db`: Nombre real de tu base de datos
- `tu-clave-secreta-super-segura`: Genera una clave secreta segura

### 3.3 Variables de entorno explicadas

#### **Variables Obligatorias:**

1. **`DATABASE_URL`** - URL de conexión a PostgreSQL

   - Formato: `postgresql://usuario:contraseña@host:puerto/base_datos`
   - Ejemplo: `postgresql://postgres:mipassword@postgres:5432/laive_db`

2. **`SECRET_KEY`** - Clave secreta para seguridad
   - Debe ser una cadena segura de al menos 32 caracteres
   - Nunca uses la clave por defecto en producción

#### **Variables Opcionales (con valores por defecto):**

3. **`ENVIRONMENT`** - Entorno de ejecución

   - Valores: `development`, `production`, `staging`
   - Por defecto: `development`
   - Recomendado: `production` para producción

4. **`DEBUG`** - Modo debug

   - Valores: `true`, `false`
   - Por defecto: `true`
   - Recomendado: `false` en producción

5. **`LOG_LEVEL`** - Nivel de logging
   - Valores: `debug`, `info`, `warning`, `error`
   - Por defecto: `debug`
   - Recomendado: `info` en producción

#### **Variables de Pool de Conexiones (Opcionales):**

6. **`DB_POOL_SIZE`** - Tamaño del pool de conexiones

   - Por defecto: `10`
   - Recomendado: `10-20` según carga

7. **`DB_MAX_OVERFLOW`** - Máximo de conexiones adicionales

   - Por defecto: `20`
   - Recomendado: `20-30` según carga

8. **`DB_POOL_TIMEOUT`** - Timeout del pool en segundos
   - Por defecto: `30`
   - Recomendado: `30-60` según red

### 3.4 Generar clave secreta segura

Puedes generar una clave secreta segura con:

```bash
# En tu terminal local
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## 🔗 Paso 4: Configurar Servicios

### 4.1 Servicio de la API

EasyPanel leerá automáticamente el archivo `easypanel.yml` que contiene:

```yaml
name: laive-api
description: API de Laive con FastAPI

services:
  - name: api
    type: app
    source:
      type: image
      image: laive-api:latest
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=${DATABASE_URL}
      - SECRET_KEY=${SECRET_KEY}
      - ENVIRONMENT=${ENVIRONMENT}
      - DEBUG=${DEBUG}
      - LOG_LEVEL=${LOG_LEVEL}
    healthcheck:
      path: /
      port: 8000
      interval: 30s
      timeout: 10s
      retries: 3
```

### 4.2 Verificar configuración

1. **Puertos expuestos:**

   - **API:** `8000` (público)
   - **Base de datos:** Usar la existente en EasyPanel

2. **Health Checks:**
   - Path: `/`
   - Puerto: `8000`
   - Intervalo: `30s`
   - Timeout: `10s`
   - Reintentos: `3`

---

## 🌍 Paso 5: Configurar Dominio (Opcional)

### 5.1 Dominio personalizado

1. Ve a la sección **"Domains"**
2. Agrega tu dominio: `api.tudominio.com`
3. Configura los registros DNS:
   ```
   A     api.tudominio.com    [IP_DEL_SERVIDOR]
   ```

### 5.2 SSL/HTTPS

1. EasyPanel configurará automáticamente SSL
2. Verifica que el certificado esté activo

---

## 🚀 Paso 6: Desplegar

### 6.1 Iniciar despliegue

1. Haz clic en **"Deploy"**
2. Espera a que se complete el build
3. Verifica que todos los servicios estén en estado "Running"

### 6.2 Verificar despliegue

```bash
# Verificar que la API responde
curl https://tu-dominio.com/

# Verificar documentación
curl https://tu-dominio.com/docs

# Verificar health check
curl https://tu-dominio.com/

# Verificar endpoint de períodos
curl https://tu-dominio.com/periodos
```

---

## 🔍 Paso 7: Monitoreo y Logs

### 7.1 Ver logs en tiempo real

1. Ve a la sección **"Logs"**
2. Selecciona el servicio `api`
3. Monitorea los logs para detectar errores

### 7.2 Comandos útiles

```bash
# Ver logs de la API
docker logs -f api

# Verificar estado de los servicios
docker ps

# Verificar conectividad con la base de datos
docker exec -it api python -c "from laive.database.config import engine; print('DB conectada')"

# Verificar variables de entorno
docker exec -it api env | grep -E "(DATABASE|SECRET|ENVIRONMENT)"
```

---

## 🛠️ Paso 8: Troubleshooting

### 8.1 Problemas comunes

**❌ Error: "Cannot connect to database"**

- Verifica que tu base de datos PostgreSQL existente esté corriendo en EasyPanel
- Verifica la variable `DATABASE_URL` con los datos correctos de tu BD
- Verifica que el host y puerto de la base de datos sean accesibles
- Revisa los logs de la aplicación para errores de conexión

**❌ Error: "Port already in use"**

- Verifica que el puerto 8000 esté libre
- Cambia el puerto si es necesario en `easypanel.yml`

**❌ Error: "Build failed"**

- Verifica que el Dockerfile esté correcto
- Revisa los logs del build
- Verifica que todas las dependencias estén en `pyproject.toml`

**❌ Error: "Environment variables not found"**

- Verifica que todas las variables estén configuradas en EasyPanel
- Asegúrate de que los nombres coincidan con los del `easypanel.yml`

### 8.2 Comandos de diagnóstico

```bash
# Verificar logs de la aplicación
docker logs api

# Verificar variables de entorno
docker exec -it api env | grep -E "(DATABASE|SECRET|ENVIRONMENT|DEBUG)"

# Verificar conectividad con la base de datos
docker exec -it api python -c "from laive.database.config import engine; print('DB conectada')"

# Verificar configuración de la aplicación
docker exec -it api python -c "from laive.database.config import DATABASE_URL, ENVIRONMENT, DEBUG; print(f'DB: {DATABASE_URL[:20]}...', f'ENV: {ENVIRONMENT}', f'DEBUG: {DEBUG}')"
```

---

## 📊 Paso 9: Verificar Funcionamiento

### 9.1 Endpoints disponibles

- **Health Check:** `GET /`
- **Documentación:** `GET /docs`
- **Períodos:** `GET /periodos`

### 9.2 Pruebas de la API

```bash
# Probar endpoint principal
curl https://tu-dominio.com/

# Probar endpoint de períodos
curl https://tu-dominio.com/periodos

# Ver documentación interactiva
# Abrir en navegador: https://tu-dominio.com/docs
```

### 9.3 Verificar configuración

```bash
# Verificar que las variables de entorno están configuradas
curl -s https://tu-dominio.com/ | jq .

# Verificar logs sin errores
# En EasyPanel → Logs → api
```

---

## 🔄 Paso 10: Actualizaciones

### 10.1 Desplegar actualizaciones

1. Haz cambios en tu código
2. Sube al repositorio: `git push origin main`
3. EasyPanel detectará automáticamente los cambios
4. Se desplegará automáticamente

### 10.2 Rollback (si es necesario)

1. Ve a la sección **"Deployments"**
2. Selecciona una versión anterior
3. Haz clic en **"Rollback"**

---

## 📞 Soporte

### En caso de problemas:

1. Revisa los logs en EasyPanel
2. Verifica la configuración de variables de entorno
3. Consulta la documentación de EasyPanel
4. Contacta al soporte de EasyPanel

### Recursos útiles:

- [Documentación de EasyPanel](https://docs.easypanel.io)
- [Documentación de FastAPI](https://fastapi.tiangolo.com)
- [Documentación de PostgreSQL](https://www.postgresql.org/docs)

---

## ✅ Checklist de Despliegue

- [ ] Repositorio subido a Git
- [ ] Proyecto creado en EasyPanel
- [ ] Repositorio conectado
- [ ] Base de datos PostgreSQL existente verificada
- [ ] Variables de entorno configuradas en EasyPanel:
  - [ ] `DATABASE_URL` con datos reales
  - [ ] `SECRET_KEY` generada segura
  - [ ] `ENVIRONMENT=production`
  - [ ] `DEBUG=false`
  - [ ] `LOG_LEVEL=info`
  - [ ] Variables de pool opcionales configuradas
- [ ] Servicio API configurado automáticamente
- [ ] Puertos configurados (8000)
- [ ] Health checks configurados
- [ ] Dominio configurado (opcional)
- [ ] SSL configurado
- [ ] Despliegue exitoso
- [ ] API responde correctamente
- [ ] Base de datos conectada
- [ ] Logs sin errores
- [ ] Endpoints funcionando:
  - [ ] Health check (`/`)
  - [ ] Documentación (`/docs`)
  - [ ] Períodos (`/periodos`)

¡Tu aplicación Laive API está lista para producción! 🎉

---

## 🔧 Configuración Avanzada

### Variables de entorno adicionales

Si necesitas más configuración, puedes agregar estas variables:

```bash
# Configuración de pool de base de datos más específica
DB_POOL_SIZE=20
DB_MAX_OVERFLOW=30
DB_POOL_TIMEOUT=60
```

### Monitoreo adicional

1. **Configurar alertas** en EasyPanel
2. **Configurar backups** de la base de datos
3. **Configurar logs** externos si es necesario
