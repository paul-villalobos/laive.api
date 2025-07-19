# 🚀 Guía de Despliegue en EasyPanel

Esta guía te ayudará a desplegar tu aplicación Laive API en EasyPanel paso a paso.

## 📋 Prerrequisitos

- ✅ Cuenta en EasyPanel
- ✅ Repositorio Git (GitHub, GitLab, etc.)
- ✅ Código subido al repositorio
- ✅ Acceso SSH al servidor (si es necesario)

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
└── README.md              ✅
```

### 1.2 Subir cambios al repositorio

```bash
git add .
git commit -m "Preparar para despliegue en EasyPanel"
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

## ⚙️ Paso 3: Configurar Servicios

### 3.1 Servicio de la API

1. **Configurar el servicio principal:**

   - Tipo: `App`
   - Nombre: `api`
   - Puerto: `8000`
   - Build Command: `docker build -t laive-api .`
   - Start Command: `docker run -p 8000:8000 laive-api`

2. **Configurar variables de entorno:**

   ```
   DATABASE_URL=postgresql://postgres:tu_password@tu_host_postgres:5432/tu_nombre_db
   ```

   **Nota:** Reemplaza los valores con los de tu base de datos existente:

   - `tu_password`: Contraseña de tu base de datos
   - `tu_host_postgres`: Host de tu base de datos PostgreSQL en EasyPanel
   - `tu_nombre_db`: Nombre de tu base de datos existente

### 3.2 Obtener información de la base de datos existente

1. **En EasyPanel, ve a tu base de datos existente**
2. **Copia los datos de conexión:**

   - Host: `tu_host_postgres`
   - Puerto: `5432` (por defecto)
   - Usuario: `postgres` (por defecto)
   - Contraseña: `tu_password`
   - Base de datos: `tu_nombre_db`

3. **Configura la variable DATABASE_URL con estos valores**

---

## 🔗 Paso 4: Configurar Redes y Puertos

### 4.1 Puertos expuestos

- **API:** `8000` (público)
- **Base de datos:** Usar la existente en EasyPanel

### 4.2 Health Checks

Configurar health check para la API:

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
```

---

## 🛠️ Paso 8: Troubleshooting

### 8.1 Problemas comunes

**❌ Error: "Cannot connect to database"**

- Verifica que tu base de datos PostgreSQL existente esté corriendo en EasyPanel
- Verifica la variable `DATABASE_URL` con los datos correctos de tu BD
- Verifica que el host y puerto de la base de datos sean accesibles

**❌ Error: "Port already in use"**

- Verifica que el puerto 8000 esté libre
- Cambia el puerto si es necesario

**❌ Error: "Build failed"**

- Verifica que el Dockerfile esté correcto
- Revisa los logs del build
- Verifica que todas las dependencias estén en `pyproject.toml`

### 8.2 Comandos de diagnóstico

```bash
# Verificar logs de la aplicación
docker logs api

# Verificar variables de entorno
docker exec -it api env | grep DATABASE

# Verificar conectividad con la base de datos
docker exec -it api python -c "from laive.database.config import engine; print('DB conectada')"
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
- [ ] Servicio PostgreSQL configurado
- [ ] Servicio API configurado
- [ ] Variables de entorno configuradas
- [ ] Puertos configurados
- [ ] Health checks configurados
- [ ] Dominio configurado (opcional)
- [ ] SSL configurado
- [ ] Despliegue exitoso
- [ ] API responde correctamente
- [ ] Base de datos conectada
- [ ] Logs sin errores

¡Tu aplicación Laive API está lista para producción! 🎉
