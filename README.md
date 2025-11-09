# Dog Breed AI - Sistema de Recomendación de Razas

Sistema inteligente de recomendación de razas de perros usando Machine Learning.

## Requisitos Previos

- **Python 3.9+** - [Descargar aquí](https://www.python.org/downloads/)
- **pip** (incluido con Python)
- **Git** (opcional)

## 🚀 Instalación Rápida

### 1. Clonar o descargar el proyecto

```bash
git clone <repository-url>
cd app
```

### 2. Ejecutar el instalador

```bash
./install.sh
```

El script automáticamente:
- ✅ Crea un entorno virtual Python
- ✅ Instala todas las dependencias
- ✅ Descarga el dataset de Kaggle (195 razas)
- ✅ Entrena los modelos de Machine Learning

## Uso

### Iniciar el servidor

```bash
./server.sh start
```

### Detener el servidor

```bash
./server.sh stop
```

### Reiniciar el servidor

```bash
./server.sh restart
```

## Acceder a la aplicación

Una vez iniciado el servidor, abre tu navegador:

- **Página de inicio**: http://localhost:8000
- **Catálogo de razas**: http://localhost:8000/breeds
- **API Docs (Swagger)**: http://localhost:8000/docs
- **API Docs (ReDoc)**: http://localhost:8000/redoc

## Dependencias Principales

```
fastapi         # Framework web
uvicorn         # Servidor ASGI
pandas          # Procesamiento de datos
scikit-learn    # Machine Learning
jinja2          # Templates HTML
kagglehub       # Dataset de Kaggle
```

## Estructura del Proyecto

```
app/
├── main.py                    # Aplicación FastAPI
├── install.sh                 # Script de instalación
├── server.sh                  # Script de servidor
├── controllers/
│   └── dog_controller.py      # Lógica de recomendación
├── models/                    # Modelos ML entrenados
├── data/
│   └── dog_breeds_dataset.csv # Dataset (195 razas)
├── templates/                 # Páginas HTML
└── static/                    # CSS, JS, imágenes
```

## Dataset

**Fuente**: [Kaggle - Dog Breeds Dataset](https://www.kaggle.com/datasets/sujaykapadnis/dog-breeds)

- 195 razas del American Kennel Club
- 14 características por raza
- Datos normalizados (escala 1-5)

## Modelos de Machine Learning

- **KNN** (K-Nearest Neighbors) - Recomendación por similitud
- **Random Forest** - Clasificación de preferencias
- **KMeans** - Agrupación de razas similares

##  Instalación Manual (opcional)

Si prefieres instalar manualmente:

```bash
# 1. Crear entorno virtual
python3 -m venv .venv

# 2. Activar entorno virtual
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Descargar dataset
python3 download_dog_dataset.py
python3 adapt_kaggle_dataset.py

# 5. Entrenar modelos
python3 train_dog_model.py

# 6. Iniciar servidor
uvicorn main:app --reload
```

## ❓ Solución de Problemas

### Error: Python no encontrado
```bash
# Verificar instalación
python3 --version

# Si no está instalado, descargar de python.org
```

### Error: Permisos en scripts .sh
```bash
chmod +x install.sh
chmod +x server.sh
```

### Error al descargar dataset de Kaggle
Verifica tu conexión a internet. El dataset se descarga automáticamente.

## Licencia

Dataset bajo licencia de Kaggle - Fuente: American Kennel Club
