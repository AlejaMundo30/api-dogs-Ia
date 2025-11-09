import pandas as pd
import os

print("=== ADAPTANDO DATASET DE KAGGLE AL FORMATO DEL PROYECTO ===\n")

# Leer el dataset descargado de Kaggle
kaggle_df = pd.read_csv('data/dog_breeds_dataset.csv')

print(f"Dataset original: {len(kaggle_df)} razas")
print(f"Columnas originales: {list(kaggle_df.columns)}\n")

# Mapear columnas de Kaggle a nuestro formato
# El dataset de Kaggle tiene columnas diferentes, necesitamos mapearlas
column_mapping = {
    'Breed': 'breed',
    'Affectionate With Family': 'good_with_kids',  # Aproximación
    'Good With Young Children': 'good_with_kids',
    'Good With Other Dogs': 'good_with_kids',  # Usaremos promedio
    'Trainability Level': 'trainability',
    'Energy Level': 'energy_level',
    'Barking Level': 'barking_tendency',
    'Coat Grooming Frequency': 'grooming_needs',
    'Adaptability Level': 'apartment_friendly',
    'Watchdog/Protective Nature': 'watchdog_ability',
}

# Crear el nuevo DataFrame con el formato adaptado
adapted_df = pd.DataFrame()

# Breed (limpiar nombres)
adapted_df['breed'] = kaggle_df['Breed'].str.strip()

# Características numéricas (todas en escala 1-5)
adapted_df['trainability'] = kaggle_df['Trainability Level']
adapted_df['energy_level'] = kaggle_df['Energy Level']
adapted_df['barking_tendency'] = kaggle_df['Barking Level']
adapted_df['grooming_needs'] = kaggle_df['Coat Grooming Frequency']
adapted_df['apartment_friendly'] = kaggle_df['Adaptability Level']
adapted_df['watchdog_ability'] = kaggle_df['Watchdog/Protective Nature']

# Good with kids (promedio de familia, niños pequeños)
adapted_df['good_with_kids'] = (
    kaggle_df['Affectionate With Family'] + 
    kaggle_df['Good With Young Children']
) / 2
adapted_df['good_with_kids'] = adapted_df['good_with_kids'].round().astype(int)

# Size - Estimamos basándonos en el nombre de la raza (pequeño, mediano, grande)
# Para razas conocidas
size_mapping = {
    'Chihuahuas': 1, 'Toy': 1, 'Miniature': 1, 'Yorkshire': 1, 'Pomeranian': 1, 'Maltese': 1,
    'Small': 2, 'Terrier': 2, 'Dachshund': 2, 'Bulldog': 2, 'Boston': 2, 'Shih Tzu': 2,
    'Medium': 3, 'Beagle': 3, 'Border': 3, 'Cocker': 3, 'Schnauzer': 3, 'Poodle': 3,
    'Large': 4, 'Labrador': 4, 'Golden': 4, 'German Shepherd': 4, 'Boxer': 4, 'Rottweiler': 4, 'Husky': 4,
    'Giant': 5, 'Great Dane': 5, 'Mastiff': 5, 'Saint Bernard': 5
}

def estimate_size(breed_name):
    breed_lower = breed_name.lower()
    for key, size in size_mapping.items():
        if key.lower() in breed_lower:
            return size
    return 3  # Default mediano

adapted_df['size'] = adapted_df['breed'].apply(estimate_size)

# Exercise needs - Basado en energy level
adapted_df['exercise_needs'] = adapted_df['energy_level']

# Good alone - Estimamos inverso a affectionate (más independiente = mejor solo)
adapted_df['good_alone'] = 5 - kaggle_df['Affectionate With Family']
adapted_df['good_alone'] = adapted_df['good_alone'].clip(1, 5)

# Reordenar columnas en el orden correcto
final_df = adapted_df[[
    'breed', 'size', 'energy_level', 'trainability', 'good_with_kids',
    'exercise_needs', 'barking_tendency', 'grooming_needs', 
    'apartment_friendly', 'good_alone', 'watchdog_ability'
]]

# Guardar el dataset adaptado
output_path = 'data/dog_breeds_dataset_kaggle.csv'
final_df.to_csv(output_path, index=False)

print(f"✓ Dataset adaptado guardado en: {output_path}")
print(f"Total de razas: {len(final_df)}")
print(f"Columnas finales: {list(final_df.columns)}")

print("\n=== PRIMERAS 10 RAZAS ADAPTADAS ===")
print(final_df.head(10))

print("\n=== ESTADÍSTICAS ===")
print(final_df.describe())

print("\n✅ Dataset de Kaggle adaptado exitosamente!")
print("Ahora tienes 2 opciones:")
print("1. Usar el dataset original (25 razas): data/dog_breeds_dataset.csv")
print("2. Usar el dataset de Kaggle (195 razas): data/dog_breeds_dataset_kaggle.csv")
print("\nPara usar el dataset de Kaggle, renómbralo o actualiza train_dog_model.py")
