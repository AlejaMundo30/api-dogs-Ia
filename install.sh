#!/bin/bash

echo "Instalando Dog Breed AI..."

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "Python 3 no está instalado"
    exit 1
fi

echo "✓ Python encontrado"

# Crear entorno virtual
if [ ! -d ".venv" ]; then
    echo "Creando entorno virtual..."
    python3 -m venv .venv
fi

# Activar entorno virtual
source .venv/bin/activate

# Instalar dependencias
echo "Instalando dependencias..."
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

# Descargar dataset si no existe
if [ ! -f "data/dog_breeds_dataset.csv" ]; then
    echo "Descargando dataset de Kaggle..."
    python3 download_dog_dataset.py
    python3 adapt_kaggle_dataset.py
fi

# Entrenar modelos si no existen
if [ ! -f "models/dog_knn_model.pkl" ]; then
    echo "Entrenando modelos ML..."
    python3 train_dog_model.py
fi

echo ""
echo "Instalación completada"
echo ""
echo "Para iniciar el servidor:"
echo "  source .venv/bin/activate"
echo "  uvicorn main:app --reload"
echo ""
