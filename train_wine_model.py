import joblib
from sklearn.datasets import load_wine
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import os

model_folder = 'models'

# Crear la carpeta 'models' si no existe
if not os.path.exists(model_folder):
    os.makedirs(model_folder)

# Cargar el dataset de Vino
wine = load_wine()
X = wine.data  # Las características del vino
y = wine.target  # Las clases de vino (0, 1, 2)

print("=== DATASET DE VINO ===")
print(f"Características: {wine.feature_names}")
print(f"Clases: {wine.target_names}")
print(f"Forma de los datos: {X.shape}")

# ===== MODELO KMEANS (No supervisado) =====
print("\n=== ENTRENANDO MODELO KMEANS ===")
kmeans = KMeans(n_clusters=3, random_state=42)  # 3 clusters para 3 tipos de vino
kmeans.fit(X)

# Guardar el modelo KMeans
joblib.dump(kmeans, f'{model_folder}/wine_kmeans_model.pkl')
print("Modelo KMeans de vino entrenado y guardado exitosamente")

# ===== MODELO KNN (Supervisado) =====
print("\n=== ENTRENANDO MODELO KNN ===")
# Dividir datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear el modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)

# Entrenar el modelo
knn.fit(X_train, y_train)

# Evaluar el modelo
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del modelo KNN: {accuracy:.4f}")

# Guardar el modelo KNN
joblib.dump(knn, f'{model_folder}/wine_knn_model.pkl')
print("Modelo KNN de vino entrenado y guardado exitosamente")

print(f"\n=== MODELOS GUARDADOS EN '{model_folder}/' ===")
print("- wine_kmeans_model.pkl (clustering)")
print("- wine_knn_model.pkl (clasificación)")