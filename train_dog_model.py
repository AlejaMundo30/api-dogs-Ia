import joblib
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
import os

model_folder = 'models'

# Crear la carpeta 'models' si no existe
if not os.path.exists(model_folder):
    os.makedirs(model_folder)

print("=== ENTRENANDO MODELOS PARA RECOMENDACIÓN DE RAZAS DE PERROS ===\n")

# Cargar el dataset
df = pd.read_csv('data/dog_breeds_dataset.csv')
print(f"Dataset cargado: {len(df)} razas de perros")
print(f"Características: {list(df.columns)[1:]}")

# Preparar los datos
X = df.drop('breed', axis=1).to_numpy()  # Características
y = df['breed'].to_numpy()  # Razas (etiquetas)
breed_names = df['breed'].unique()

print(f"\nRazas incluidas ({len(breed_names)}):")
for i, breed in enumerate(breed_names):
    print(f"{i+1:2}. {breed}")

# Normalizar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Guardar el scaler
joblib.dump(scaler, f'{model_folder}/dog_scaler.pkl')
print(f"\nScaler guardado en {model_folder}/dog_scaler.pkl")

# ===== MODELO KMEANS (Clustering de perros similares) =====
print("\n=== ENTRENANDO MODELO KMEANS (CLUSTERING) ===")
kmeans = KMeans(n_clusters=5, random_state=42)  # 5 grupos de perros similares
kmeans.fit(X_scaled)

# Guardar el modelo KMeans
joblib.dump(kmeans, f'{model_folder}/dog_kmeans_model.pkl')
print("✓ Modelo KMeans guardado para agrupar perros similares")

# ===== MODELO RANDOM FOREST (Clasificación de razas) =====
print("\n=== ENTRENANDO MODELO RANDOM FOREST ===")
# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Crear y entrenar modelo
rf_model = RandomForestClassifier(n_estimators=100, random_state=42, min_samples_leaf=1, max_features='sqrt')
rf_model.fit(X_train, y_train)

# Evaluar modelo
y_pred = rf_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✓ Precisión del modelo Random Forest: {accuracy:.4f}")

# Guardar el modelo
joblib.dump(rf_model, f'{model_folder}/dog_rf_model.pkl')

# ===== MODELO KNN (Recomendación basada en similitud) =====
print("\n=== ENTRENANDO MODELO KNN ===")
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X_train, y_train)

# Evaluar KNN
y_pred_knn = knn_model.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)
print(f"✓ Precisión del modelo KNN: {accuracy_knn:.4f}")

# Guardar el modelo KNN
joblib.dump(knn_model, f'{model_folder}/dog_knn_model.pkl')

# Guardar información adicional
breed_info = {
    'breeds': list(breed_names),
    'features': list(df.columns)[1:],
    'feature_descriptions': {
        'size': 'Tamaño (1=muy pequeño, 5=muy grande)',
        'energy_level': 'Nivel de energía (1=tranquilo, 5=muy activo)',
        'trainability': 'Facilidad de entrenamiento (1=difícil, 5=fácil)',
        'good_with_kids': 'Bueno con niños (1=no recomendado, 5=excelente)',
        'exercise_needs': 'Necesidades de ejercicio (1=poco, 5=mucho)',
        'barking_tendency': 'Tendencia a ladrar (1=silencioso, 5=ladra mucho)',
        'grooming_needs': 'Necesidades de cuidado (1=poco, 5=mucho)',
        'apartment_friendly': 'Apto para apartamento (1=no, 5=perfecto)',
        'good_alone': 'Tolera estar solo (1=no tolera, 5=muy independiente)',
        'watchdog_ability': 'Capacidad de guardia (1=no protector, 5=excelente guardián)'
    }
}

import json
with open(f'{model_folder}/breed_info.json', 'w', encoding='utf-8') as f:
    json.dump(breed_info, f, ensure_ascii=False, indent=2)

print("\n=== RESUMEN DE MODELOS ENTRENADOS ===")
print("✓ KMeans: Clustering de razas similares")
print(f"✓ Random Forest: Clasificación de razas (precisión: {accuracy:.4f})")
print(f"✓ KNN: Recomendación por similitud (precisión: {accuracy_knn:.4f})")
print("✓ Scaler: Normalización de características")
print("✓ Información de razas: JSON con metadatos")

print(f"\nTodos los modelos guardados en '{model_folder}/'")