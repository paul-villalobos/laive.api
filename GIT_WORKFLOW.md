# Git Workflow - Solo Desarrollador

## 📋 Resumen del Flujo

```
main (producción) ← develop ← feature/nueva-funcionalidad
```

## 🎯 Branches Principales

- **`main`**: Código en producción (se deploya automáticamente)
- **`develop`**: Rama de desarrollo integrado
- **`feature/*`**: Rama temporal para nuevas funcionalidades

## 🚀 Workflow Diario

### 1. Inicio del día

```bash
# Actualizar develop con los últimos cambios
git checkout develop
git pull origin develop
```

### 2. Crear nueva feature

```bash
# Crear y cambiar a nueva rama de feature
git checkout -b feature/nombre-descriptivo

# Ejemplos:
git checkout -b feature/user-authentication
git checkout -b feature/api-endpoints
git checkout -b feature/database-models
```

### 3. Desarrollar y hacer commits

```bash
# Hacer cambios en tu código...

# Commits descriptivos y atómicos
git add .
git commit -m "feat: agregar endpoint de login"
git commit -m "fix: corregir validación de email"
git commit -m "docs: actualizar documentación API"
git commit -m "refactor: limpiar código de autenticación"
```

### 4. Finalizar feature

```bash
# Cambiar a develop
git checkout develop

# Mergear feature a develop
git merge feature/nombre-descriptivo

# Subir cambios
git push origin develop

# Eliminar rama de feature (opcional)
git branch -d feature/nombre-descriptivo
```

### 5. Deploy a producción

```bash
# Cuando esté listo para producción
git checkout main
git merge develop
git push origin main  # ← Esto dispara el deploy automático
```

## 📝 Convenciones de Commits

### Tipos de commits:

- `feat`: Nueva funcionalidad
- `fix`: Corrección de bug
- `docs`: Documentación
- `style`: Formato de código
- `refactor`: Refactorización
- `test`: Tests
- `chore`: Tareas de mantenimiento

### Ejemplos:

```bash
git commit -m "feat: agregar autenticación JWT"
git commit -m "fix: resolver error de conexión a base de datos"
git commit -m "docs: actualizar README con instrucciones de deploy"
git commit -m "refactor: simplificar lógica de validación"
```

## 🚨 Hotfixes (Correcciones Urgentes)

### Para bugs críticos en producción:

```bash
# Crear hotfix desde main
git checkout main
git pull origin main
git checkout -b hotfix/critical-bug-fix

# Arreglar el bug
# ... hacer cambios ...
git commit -m "fix: parchear vulnerabilidad de seguridad"

# Mergear a main (deploy inmediato)
git checkout main
git merge hotfix/critical-bug-fix
git push origin main

# Mergear también a develop
git checkout develop
git merge hotfix/critical-bug-fix
git push origin develop

# Eliminar rama de hotfix
git branch -d hotfix/critical-bug-fix
```

## 🔄 Comandos Útiles

### Ver estado actual:

```bash
git status
git branch -a  # Ver todas las ramas
git log --oneline -10  # Ver últimos 10 commits
```

### Cambiar entre ramas:

```bash
git checkout develop
git checkout feature/nombre-feature
git checkout main
```

### Ver diferencias:

```bash
git diff  # Ver cambios no staged
git diff --staged  # Ver cambios staged
git diff develop..feature/nombre-feature  # Ver diferencias entre ramas
```

## ⚠️ Reglas Importantes

1. **Nunca trabajar directamente en `main`**
2. **Siempre hacer pull antes de crear nueva feature**
3. **Commits atómicos y descriptivos**
4. **Mergear solo features completas a `develop`**
5. **Probar en `develop` antes de mergear a `main`**

## 🎯 Flujo Completo Ejemplo

```bash
# 1. Inicio
git checkout develop
git pull origin develop

# 2. Nueva feature
git checkout -b feature/user-registration

# 3. Desarrollar
# ... escribir código ...
git add .
git commit -m "feat: agregar modelo de usuario"
git commit -m "feat: implementar endpoint de registro"
git commit -m "test: agregar tests para registro"

# 4. Finalizar feature
git checkout develop
git merge feature/user-registration
git push origin develop

# 5. Deploy (cuando esté listo)
git checkout main
git merge develop
git push origin main

# 6. Limpiar
git branch -d feature/user-registration
```

## 📚 Comandos de Emergencia

### Descartar cambios:

```bash
git checkout -- .  # Descartar todos los cambios
git reset --hard HEAD  # Resetear al último commit
```

### Ver historial:

```bash
git log --graph --oneline --all  # Ver árbol de commits
git show <commit-hash>  # Ver detalles de un commit
```

---

**Nota**: Este workflow está optimizado para un solo desarrollador con deploy automático en `main`.
