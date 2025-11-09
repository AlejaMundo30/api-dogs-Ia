import pandas as pd
import numpy as np
import os
import kagglehub

print("=== DESCARGANDO DATASET REAL DE RAZAS DE PERROS DESDE KAGGLE ===\n")

# Crear directorio para datos si no existe
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

try:
    print("Descargando dataset desde Kaggle...")
    print("Dataset: sujaykapadnis/dog-breeds")
    print("Esto puede tomar unos momentos...\n")
    
    # Descargar el dataset usando la nueva API
    path = kagglehub.dataset_download("sujaykapadnis/dog-breeds")
    
    print(f"✓ Dataset descargado en: {path}")
    
    # Buscar el archivo breed_traits.csv (el que tiene las características de las razas)
    csv_file = os.path.join(path, "breed_traits.csv")
    
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"No se encontró breed_traits.csv en {path}")
    
    print(f"Archivo CSV encontrado: {csv_file}")
    
    # Leer el dataset
    df = pd.read_csv(csv_file)
    
    print("✓ Dataset cargado exitosamente desde Kaggle!")
    print(f"Número de razas: {len(df)}")
    print(f"Columnas disponibles: {list(df.columns)}")
    
    # Mostrar primeras filas
    print("\n=== PRIMERAS 5 RAZAS DEL DATASET REAL ===")
    print(df.head())
    
    print("\n=== INFORMACIÓN DEL DATASET ===")
    print(df.info())
    
    print("\n=== ESTADÍSTICAS BÁSICAS ===")
    print(df.describe())
    
    # Guardar el dataset localmente
    csv_path = f'{data_dir}/dog_breeds_dataset.csv'
    df.to_csv(csv_path, index=False)
    print(f"\n✓ Dataset guardado en: {csv_path}")
    
    print("\n=== DATASET REAL DE KAGGLE LISTO PARA USAR ===")
    print("Ahora puedes entrenar el modelo con datos reales ejecutando:")
    print("python train_dog_model.py")
    
except Exception as e:
    print(f"\n❌ Error al descargar el dataset de Kaggle: {e}")
    print("\nPosibles soluciones:")
    print("1. Asegúrate de tener instalado kagglehub: pip install kagglehub")
    print("2. Configura tus credenciales de Kaggle si es necesario")
    print("3. Verifica tu conexión a internet")
    print("\nMás información: https://github.com/Kaggle/kagglehub")