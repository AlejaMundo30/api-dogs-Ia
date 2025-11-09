# Manual de Instalación y Despliegue - Dog Breed AI

**Proyecto**: Sistema de Recomendación de Razas de Perros con Machine Learning  
**Institución**: Tecnológico de Antioquia  
**Autores**: Alejandra Orrego, Stiven Aguirre, Kevin

---

## Tabla de Contenidos
1. [Requisitos del Sistema](#requisitos-del-sistema)
2. [Instalación Automática](#instalación-automática)
3. [Instalación Manual](#instalación-manual)
4. [Configuración del Proyecto](#configuración-del-proyecto)
5. [Ejecución del Servidor](#ejecución-del-servidor)
6. [Verificación de la Instalación](#verificación-de-la-instalación)
7. [Solución de Problemas](#solución-de-problemas)

---

## Requisitos del Sistema

### Software Necesario

| Componente | Versión Mínima | Versión Recomendada | Descarga |
|------------|---------------|---------------------|----------|
| **Python** | 3.9.0 | 3.11+ | https://www.python.org/downloads/ |
| **pip** | 21.0+ | Latest | Incluido con Python |
| **Git** | 2.0+ (opcional) | Latest | https://git-scm.com/downloads |

### Sistemas Operativos Soportados
- macOS 10.15+
- Linux (Ubuntu 20.04+, Debian 10+, CentOS 8+)
- Windows 10/11

### Requisitos de Hardware
- **RAM**: Mínimo 2GB, recomendado 4GB+
- **Disco**: 500MB libres para dependencias y modelos
- **CPU**: Cualquier procesador moderno (x86_64, ARM64)

### Verificar Python Instalado

```bash
# Verificar versión de Python
python3 --version
# Salida esperada: Python 3.9.x o superior

# Verificar pip
pip3 --version
# Salida esperada: pip 21.x o superior
```

---

## Instalación Automática

### Método Recomendado (Script de Instalación)

**Paso 1**: Descargar o clonar el proyecto

```bash
# Opción A: Clonar con Git
git clone <repository-url>
cd app

# Opción B: Descargar ZIP y extraer
# Navegar a la carpeta del proyecto
cd /ruta/a/dog-breed-ai/app
```

**Paso 2**: Dar permisos de ejecución al script

```bash
chmod +x install.sh
```

**Paso 3**: Ejecutar el instalador

```bash
./install.sh
```

### ¿Qué Hace el Script Automático?

El script `install.sh` realiza las siguientes tareas:

1. ****Verifica Python 3.9+** está instalado
2. ****Crea entorno virtual** en `.venv/`
3. ****Actualiza pip** a la última versión
4. ****Instala dependencias** desde `requirements.txt`
5. ****Descarga dataset** de Kaggle (195 razas)
6. ****Adapta dataset** al formato del proyecto
7. ****Entrena modelos ML** (KNN, Random Forest, KMeans)
8. ****Genera archivos .pkl** en carpeta `models/`

**Tiempo estimado**: 5-10 minutos (dependiendo de conexión a internet)

---

## Instalación Manual

Si prefieres instalar paso a paso:

### Paso 1: Crear Entorno Virtual

```bash
# Navegar al directorio del proyecto
cd /ruta/a/dog-breed-ai/app

# Crear entorno virtual
python3 -m venv .venv

# Verificar creación
ls -la | grep .venv
```

### Paso 2: Activar Entorno Virtual

**En macOS/Linux:**
```bash
source .venv/bin/activate
```

**En Windows:**
```cmd
.venv\Scripts\activate
```

**Verificación**: El prompt debe mostrar `(.venv)` al inicio

```bash
(.venv) user@machine:~/app$
```

### Paso 3: Actualizar pip

```bash
pip install --upgrade pip
```

### Paso 4: Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Dependencias que se instalarán:**

```
fastapi==0.104.1          # Framework web
uvicorn[standard]==0.24.0 # Servidor ASGI
pandas==2.1.3             # Procesamiento de datos
scikit-learn==1.3.2       # Machine Learning
jinja2==3.1.2             # Templates HTML
python-multipart==0.0.6   # Formularios HTML
joblib==1.3.2             # Persistencia de modelos
kagglehub==0.2.9          # Descarga de Kaggle
```

### Paso 5: Descargar y Preparar Dataset

```bash
# Descargar desde Kaggle
python3 download_dog_dataset.py

# Adaptar al formato del proyecto
python3 adapt_kaggle_dataset.py
```

**Archivos generados:**
- `data/dog_breeds_dataset.csv` (7.5KB, 195 razas)

### Paso 6: Entrenar Modelos de Machine Learning

```bash
python3 train_dog_model.py
```

**Modelos generados en `models/`:**
- `dog_knn_model.pkl` - K-Nearest Neighbors
- `dog_random_forest.pkl` - Random Forest Classifier
- `dog_kmeans_model.pkl` - KMeans Clustering
- `dog_scaler.pkl` - StandardScaler (normalización)

**Salida esperada:**
```
✓ Dataset cargado: 195 razas
✓ Modelos entrenados correctamente
  - KNN accuracy: ~95%
  - Random Forest accuracy: ~92%
  - KMeans clusters: 5
✓ Modelos guardados en models/
```

---

## Configuración del Proyecto

### Estructura de Directorios

Después de la instalación, el proyecto debe tener esta estructura:

```
app/
├── .venv/                     # Entorno virtual (generado)
├── main.py                    # Aplicación FastAPI principal
├── install.sh                 # Script de instalación
├── server.sh                  # Script de servidor
├── requirements.txt           # Dependencias Python
│
├── controllers/
│   └── dog_controller.py      # Lógica de negocio ML
│
├── models/                    # Modelos entrenados (generado)
│   ├── dog_knn_model.pkl
│   ├── dog_random_forest.pkl
│   ├── dog_kmeans_model.pkl
│   └── dog_scaler.pkl
│
├── data/
│   └── dog_breeds_dataset.csv # Dataset 195 razas (generado)
│
├── templates/                 # Plantillas HTML
│   ├── dog_home.html
│   ├── dog_breeds.html
│   ├── dog_results.html
│   └── index.html
│
├── static/                    # Recursos estáticos
│   ├── css/
│   ├── js/
│   └── images/
│
└── docs/                      # Documentación
    └── 01_ARQUITECTURA.md
```

### Variables de Entorno (Opcional)

Crear archivo `.env` para configuraciones personalizadas:

```bash
# .env
HOST=0.0.0.0
PORT=8000
RELOAD=true
LOG_LEVEL=info
```

---

## Ejecución del Servidor

### Método 1: Script Automático (Recomendado)

```bash
# Iniciar servidor
./server.sh start

# Detener servidor
./server.sh stop

# Reiniciar servidor
./server.sh restart
```

### Método 2: Uvicorn Directo

**Desarrollo (con hot reload):**
```bash
# Activar entorno virtual
source .venv/bin/activate

# Iniciar servidor
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```

**Producción (multi-worker):**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Opciones de Uvicorn

| Opción | Descripción | Ejemplo |
|--------|-------------|---------|
| `--reload` | Hot reload en cambios | Desarrollo |
| `--host` | IP de escucha | `0.0.0.0` o `127.0.0.1` |
| `--port` | Puerto HTTP | `8000` (default) |
| `--workers` | Procesos paralelos | `4` (producción) |
| `--log-level` | Nivel de logs | `info`, `debug`, `warning` |

### Salida Esperada al Iniciar

```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

---

## Verificación de la Instalación

### 1. Verificar Archivos Esenciales

```bash
# Ejecutar desde el directorio del proyecto
ls -lh models/*.pkl
ls -lh data/dog_breeds_dataset.csv
```

**Salida esperada:**
```
-rw-r--r--  dog_knn_model.pkl       (45KB)
-rw-r--r--  dog_random_forest.pkl   (120KB)
-rw-r--r--  dog_kmeans_model.pkl    (12KB)
-rw-r--r--  dog_scaler.pkl          (2KB)
-rw-r--r--  dog_breeds_dataset.csv  (7.5KB)
```

### 2. Probar Endpoints

```bash
# Test página de inicio
curl http://localhost:8000/

# Test endpoint de salud
curl http://localhost:8000/breeds

# Test API docs
curl http://localhost:8000/docs
```

### 3. Acceder desde Navegador

Abrir las siguientes URLs:

- **Home**: http://localhost:8000
- **Catálogo**: http://localhost:8000/breeds
- **API Docs**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

****Instalación exitosa** si todas las páginas cargan correctamente

---

## Solución de Problemas

### Error: "Python 3 no está instalado"

**Solución:**
```bash
# Instalar Python desde python.org
# macOS con Homebrew:
brew install python@3.11

# Ubuntu/Debian:
sudo apt update
sudo apt install python3.11 python3-pip

# Verificar instalación
python3 --version
```

### Error: "No module named 'fastapi'"

**Causa**: Entorno virtual no activado o dependencias no instaladas

**Solución:**
```bash
# Activar entorno virtual
source .venv/bin/activate

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: "Address already in use"

**Causa**: Puerto 8000 ocupado por otro proceso

**Solución:**
```bash
# Opción 1: Matar proceso en puerto 8000
lsof -ti:8000 | xargs kill -9

# Opción 2: Usar otro puerto
uvicorn main:app --reload --port 8001
```

### Error: "Permission denied" al ejecutar install.sh

**Solución:**
```bash
# Dar permisos de ejecución
chmod +x install.sh
chmod +x server.sh

# Ejecutar
./install.sh
```

### Error: "Failed to download dataset from Kaggle"

**Causa**: Conexión a internet o límite de Kaggle

**Solución:**
```bash
# Verificar conexión
ping kaggle.com

# Intentar descarga manual desde:
# https://www.kaggle.com/datasets/sujaykapadnis/dog-breeds

# Colocar breed_traits.csv en carpeta raíz
# Ejecutar adaptación:
python3 adapt_kaggle_dataset.py
```

### Error: ModuleNotFoundError en Windows

**Causa**: Paths con espacios o caracteres especiales

**Solución:**
```bash
# Usar ruta corta sin espacios
cd C:\Projects\dog-breed-ai\app

# Recrear entorno virtual
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Logs de Depuración

```bash
# Ejecutar con logs detallados
uvicorn main:app --reload --log-level debug

# Ver salida de entrenamiento
python3 train_dog_model.py --verbose
```

---

## Desinstalación

Para remover completamente el proyecto:

```bash
# Desactivar entorno virtual
deactivate

# Eliminar entorno virtual
rm -rf .venv

# Eliminar modelos generados
rm -rf models/*.pkl

# Eliminar dataset
rm -f data/dog_breeds_dataset.csv

# Opcional: Eliminar todo el proyecto
cd ..
rm -rf app/
```

---

## Próximos Pasos

Una vez instalado exitosamente:

1. 📖 Leer el [Manual de Usuario](02_MANUAL_USUARIO.md)
2. Consultar la [Documentación Técnica](03_DOCUMENTACION_TECNICA.md)
3. Revisar el [Manual de Datos](04_MANUAL_DATOS.md)
4. Empezar a usar la API

---

**¿Problemas?** Abre un issue en el repositorio con:
- Sistema operativo y versión
- Versión de Python
- Mensaje de error completo
- Salida de `pip list`
