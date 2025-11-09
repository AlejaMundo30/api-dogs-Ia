import pandas as pd
import numpy as np
import os
from urllib.request import urlretrieve
import zipfile

print("=== PREPARANDO DATASET DE RAZAS DE PERROS ===\n")

# Crear directorio para datos si no existe
data_dir = 'data'
if not os.path.exists(data_dir):
    os.makedirs(data_dir)

# URL del dataset (versión CSV simplificada)
# Como no podemos descargar directamente de Kaggle sin API key, 
# vamos a crear un dataset simulado basado en el original
print("Creando dataset simulado basado en razas de perros...")

# Definir razas populares y sus características
dog_data = {
    'breed': [
        'Golden Retriever', 'Bulldog Francés', 'Pastor Alemán', 'Labrador Retriever',
        'Chihuahua', 'Poodle', 'Rottweiler', 'Beagle', 'Yorkshire Terrier',
        'Boxer', 'Husky Siberiano', 'Border Collie', 'Dachshund', 'Shih Tzu',
        'Boston Terrier', 'Pomeranian', 'Australian Shepherd', 'Siberian Husky',
        'Cocker Spaniel', 'Maltese', 'Jack Russell Terrier', 'Pit Bull',
        'Great Dane', 'Doberman', 'Schnauzer'
    ],
    # Características en escala 1-5
    'size': [4, 2, 4, 4, 1, 3, 5, 3, 1, 4, 4, 3, 2, 2, 2, 1, 4, 4, 3, 1, 2, 4, 5, 4, 3],
    'energy_level': [4, 2, 4, 4, 3, 3, 3, 4, 3, 4, 5, 5, 3, 2, 3, 3, 5, 5, 3, 2, 5, 4, 2, 4, 3],
    'trainability': [5, 2, 5, 5, 2, 5, 4, 3, 3, 3, 3, 5, 3, 3, 4, 3, 5, 3, 4, 3, 3, 3, 3, 4, 4],
    'good_with_kids': [5, 4, 4, 5, 2, 4, 3, 5, 3, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 3, 3, 4, 3, 4],
    'exercise_needs': [4, 1, 4, 4, 2, 3, 3, 4, 2, 4, 5, 5, 3, 2, 3, 2, 5, 5, 3, 2, 4, 4, 2, 4, 3],
    'barking_tendency': [2, 2, 3, 2, 4, 2, 2, 3, 4, 2, 3, 2, 3, 3, 2, 4, 2, 3, 2, 3, 4, 2, 1, 2, 3],
    'grooming_needs': [3, 2, 3, 2, 2, 5, 2, 2, 4, 1, 3, 3, 2, 4, 1, 4, 3, 3, 3, 4, 2, 1, 1, 1, 3],
    'apartment_friendly': [3, 5, 2, 2, 5, 4, 1, 3, 5, 2, 1, 2, 4, 5, 5, 5, 2, 1, 4, 5, 3, 2, 2, 2, 4],
    'good_alone': [3, 4, 2, 3, 3, 3, 2, 2, 2, 3, 1, 2, 3, 3, 4, 2, 2, 1, 3, 2, 2, 3, 3, 3, 3],
    'watchdog_ability': [3, 2, 5, 3, 4, 2, 5, 3, 3, 4, 3, 3, 3, 2, 3, 3, 4, 3, 3, 2, 4, 4, 3, 5, 4]
}

# Crear DataFrame
df = pd.DataFrame(dog_data)

# Guardar el dataset
csv_path = f'{data_dir}/dog_breeds_dataset.csv'
df.to_csv(csv_path, index=False)

print(f"Dataset creado exitosamente: {csv_path}")
print(f"Número de razas: {len(df)}")
print(f"Características: {list(df.columns)[1:]}")

# Mostrar primeras filas
print("\n=== PRIMERAS 5 RAZAS ===")
print(df.head())

print("\n=== ESTADÍSTICAS BÁSICAS ===")
print(df.describe())

print("\n=== INFORMACIÓN DEL DATASET ===")
print("Características (escala 1-5):")
print("- size: Tamaño (1=muy pequeño, 5=muy grande)")
print("- energy_level: Nivel de energía (1=tranquilo, 5=muy activo)")
print("- trainability: Facilidad de entrenamiento (1=difícil, 5=fácil)")
print("- good_with_kids: Bueno con niños (1=no recomendado, 5=excelente)")
print("- exercise_needs: Necesidades de ejercicio (1=poco, 5=mucho)")
print("- barking_tendency: Tendencia a ladrar (1=silencioso, 5=ladra mucho)")
print("- grooming_needs: Necesidades de cuidado (1=poco, 5=mucho)")
print("- apartment_friendly: Apto para apartamento (1=no, 5=perfecto)")
print("- good_alone: Tolera estar solo (1=no tolera, 5=muy independiente)")
print("- watchdog_ability: Capacidad de guardia (1=no protector, 5=excelente guardián)")