# Manual de Preparación de Datos - Dog Breed AI

**Proyecto**: Sistema de Recomendación de Razas de Perros con Machine Learning  
**Institución**: Tecnológico de Antioquia  
**Autores**: Alejandra Orrego, Stiven Aguirre, Kevin

---

## 1. Fuente de Datos

### 1.1 Información del Dataset

**Nombre**: Dog Breeds Dataset  
**Fuente**: Kaggle - American Kennel Club (AKC)  
**Autor**: Sujay Kapadnis  
**URL**: https://www.kaggle.com/datasets/sujaykapadnis/dog-breeds  
**Licencia**: Community Data License Agreement  

### 1.2 Descripción del Dataset Original

El dataset contiene información detallada sobre **195 razas de perros** reconocidas por el American Kennel Club, con 14 características comportamentales y físicas normalizadas en escala de 1 a 5.

**Características del dataset original (Kaggle)**:

| Campo | Tipo | Rango | Descripción |
|-------|------|-------|-------------|
| `Breed` | String | - | Nombre de la raza |
| `Affectionate With Family` | Integer | 1-5 | Nivel de afecto con la familia |
| `Good With Young Children` | Integer | 1-5 | Compatibilidad con niños pequeños |
| `Good With Other Dogs` | Integer | 1-5 | Sociabilidad con otros perros |
| `Shedding Level` | Integer | 1-5 | Cantidad de pelo que suelta |
| `Coat Grooming Frequency` | Integer | 1-5 | Frecuencia de cepillado requerida |
| `Drooling Level` | Integer | 1-5 | Nivel de babeo |
| `Coat Type` | String | - | Tipo de pelaje (Smooth, Wavy, etc.) |
| `Coat Length` | String | - | Longitud del pelaje (Short, Medium, Long) |
| `Openness To Strangers` | Integer | 1-5 | Apertura a desconocidos |
| `Playfulness Level` | Integer | 1-5 | Nivel de juguetón |
| `Watchdog/Protective Nature` | Integer | 1-5 | Instinto protector |
| `Adaptability Level` | Integer | 1-5 | Capacidad de adaptación |
| `Trainability Level` | Integer | 1-5 | Facilidad de entrenamiento |
| `Energy Level` | Integer | 1-5 | Nivel de energía |
| `Barking Level` | Integer | 1-5 | Frecuencia de ladridos |
| `Mental Stimulation Needs` | Integer | 1-5 | Necesidad de estimulación mental |

**Escala de valores** (1-5):
- **1**: Muy bajo / Nunca
- **2**: Bajo / Raramente  
- **3**: Moderado / A veces
- **4**: Alto / Frecuentemente
- **5**: Muy alto / Siempre

---

## 2. Proceso de Descarga y Adaptación

### 2.1 Descarga del Dataset (`download_dog_dataset.py`)

**Script de descarga**:
```python
import kagglehub

# Descargar dataset de Kaggle
path = kagglehub.dataset_download("sujaykapadnis/dog-breeds")

print(f"Dataset descargado en: {path}")
# Típicamente: ~/.cache/kagglehub/datasets/sujaykapadnis/dog-breeds/
```

**Requisitos previos**:
1. Cuenta de Kaggle activa
2. API token de Kaggle configurado (`~/.kaggle/kaggle.json`)
3. Librería `kagglehub` instalada

**Ejecución**:
```bash
python3 download_dog_dataset.py
```

**Salida**:
```
Dataset descargado en: /Users/usuario/.cache/kagglehub/datasets/sujaykapadnis/dog-breeds/versions/1
Archivo: breed_traits.csv
```

---

### 2.2 Adaptación del Dataset (`adapt_kaggle_dataset.py`)

El dataset original de Kaggle contiene 14 características, pero nuestro sistema usa **10 características optimizadas** para el modelo de recomendación.

**Transformaciones realizadas**:

#### **a) Renombrado de columnas**
```python
# Mapeo Kaggle → Proyecto
column_mapping = {
    'Breed': 'breed',
    'Affectionate With Family': 'affectionate_level',
    'Good With Young Children': 'good_with_children',
    'Good With Other Dogs': 'good_with_other_dogs',
    'Shedding Level': 'shedding_level',
    'Openness To Strangers': 'openness_to_strangers',
    'Playfulness Level': 'playfulness',
    'Watchdog/Protective Nature': 'protectiveness',
    'Trainability Level': 'trainability',
    'Energy Level': 'energy_level',
    'Barking Level': 'barking_level'
}
```

#### **b) Cálculo de características derivadas**

**1. Size (Tamaño)** - Calculado desde descripciones textuales:
```python
def calculate_size(breed_name, description):
    """
    Estima el tamaño basado en el nombre y características
    
    Returns:
        1 = Pequeño (< 25 lbs)
        2 = Mediano (25-60 lbs)
        3 = Grande (> 60 lbs)
    """
    small_breeds = ['Chihuahua', 'Pomeranian', 'Yorkshire', 'Toy', 'Mini']
    large_breeds = ['Mastiff', 'Great Dane', 'Bernese', 'Rottweiler']
    
    if any(word in breed_name for word in small_breeds):
        return 1
    elif any(word in breed_name for word in large_breeds):
        return 3
    else:
        return 2
```

**2. Good Alone (Independencia)** - Calculado desde otras características:
```python
def calculate_good_alone(row):
    """
    Estima qué tan bien tolera estar solo
    
    Formula: Inverso de afecto + bajo nivel de ladrido
    """
    affectionate = row['affectionate_level']
    barking = row['barking_level']
    
    # Razas menos afectuosas y que ladran poco → mejor solos
    good_alone = 6 - (affectionate + barking) / 2
    
    return max(1, min(5, round(good_alone)))
```

#### **c) Selección de columnas finales**

**10 características del proyecto**:
```python
final_columns = [
    'breed',                  # Nombre de la raza
    'energy_level',           # 1-5: Energía
    'trainability',           # 1-5: Entrenabilidad
    'shedding_level',         # 1-5: Muda de pelo
    'barking_level',          # 1-5: Ladridos
    'playfulness',            # 1-5: Juguetón
    'protectiveness',         # 1-5: Protector
    'good_with_children',     # 1-5: Bueno con niños
    'good_with_other_dogs',   # 1-5: Bueno con otros perros
    'size',                   # 1-3: Pequeño/Mediano/Grande
    'good_alone'              # 1-5: Tolera soledad (calculado)
]
```

**Ejecución del script**:
```bash
python3 adapt_kaggle_dataset.py
```

**Salida**:
```
✓ Dataset adaptado correctamente
Archivo generado: data/dog_breeds_dataset.csv
Razas procesadas: 195
```

---

## 3. Formato del Dataset Final

### 3.1 Estructura del Archivo CSV

**Ubicación**: `data/dog_breeds_dataset.csv`  
**Tamaño**: ~7.5 KB  
**Filas**: 196 (195 razas + 1 header)  
**Columnas**: 10 características + 1 nombre

**Ejemplo de contenido**:
```csv
breed,energy_level,trainability,shedding_level,barking_level,playfulness,protectiveness,good_with_children,good_with_other_dogs,size,good_alone
Labrador Retriever,4,5,4,3,5,3,5,4,3,2
Golden Retriever,4,5,4,2,5,3,5,5,3,2
German Shepherd,4,5,4,3,4,5,4,3,3,2
Beagle,4,3,3,5,4,2,5,4,2,1
Bulldog,2,3,3,2,3,3,4,3,2,3
Poodle,4,5,1,3,4,3,4,4,2,3
Chihuahua,3,3,1,5,3,4,2,2,1,4
```

### 3.2 Validación del Dataset

**Script de validación**:
```python
import pandas as pd

df = pd.read_csv('data/dog_breeds_dataset.csv')

# Validar estructura
assert len(df) == 195, "Deben ser 195 razas"
assert len(df.columns) == 11, "Deben ser 11 columnas"

# Validar rangos
for col in ['energy_level', 'trainability', 'shedding_level', ...]:
    assert df[col].min() >= 1, f"{col} tiene valores < 1"
    assert df[col].max() <= 5, f"{col} tiene valores > 5"

assert df['size'].min() >= 1, "Size debe ser >= 1"
assert df['size'].max() <= 3, "Size debe ser <= 3"

print("✓ Dataset válido")
```

---

## 4. Carga de Datos en la Aplicación

### 4.1 Carga en Controller (`dog_controller.py`)

```python
import pandas as pd
import os

def load_dataset():
    """
    Carga el dataset desde CSV a DataFrame de pandas
    
    Returns:
        pd.DataFrame: Dataset con 195 razas y 10 características
    """
    dataset_path = os.path.join('data', 'dog_breeds_dataset.csv')
    
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(
            f"Dataset no encontrado en {dataset_path}. "
            "Ejecuta: python3 download_dog_dataset.py && "
            "python3 adapt_kaggle_dataset.py"
        )
    
    df = pd.read_csv(dataset_path)
    
    # Validar integridad
    required_columns = [
        'breed', 'energy_level', 'trainability', 
        'shedding_level', 'barking_level', 'playfulness',
        'protectiveness', 'good_with_children', 
        'good_with_other_dogs', 'size', 'good_alone'
    ]
    
    if not all(col in df.columns for col in required_columns):
        raise ValueError("Dataset tiene columnas faltantes")
    
    return df
```

### 4.2 Uso en Recomendación

```python
def get_recommendation(user_preferences):
    # 1. Cargar dataset
    df = load_dataset()
    
    # 2. Separar features y labels
    X = df[['energy_level', 'trainability', ...]]  # 10 features
    y = df['breed']  # 195 razas
    
    # 3. Normalizar con scaler
    scaler = joblib.load('models/dog_scaler.pkl')
    X_scaled = scaler.transform(X)
    
    # 4. Predecir con modelo
    model = joblib.load('models/dog_knn_model.pkl')
    distances, indices = model.kneighbors([user_input_scaled])
    
    # 5. Retornar top 5 razas
    recommended_breeds = y.iloc[indices[0]].tolist()
    return recommended_breeds[:5]
```

---

## 5. Estructura de Entrada del Usuario

### 5.1 Formato JSON Esperado

**Endpoint**: `POST /recommend`

**Body (JSON)**:
```json
{
  "energy_level": 4,
  "trainability": 5,
  "shedding_level": 2,
  "barking_level": 2,
  "playfulness": 4,
  "protectiveness": 3,
  "good_with_children": 5,
  "good_with_other_dogs": 4,
  "size": 2,
  "good_alone": 3
}
```

**Validación con Pydantic**:
```python
from pydantic import BaseModel, validator

class DogPreferences(BaseModel):
    energy_level: int
    trainability: int
    shedding_level: int
    barking_level: int
    playfulness: int
    protectiveness: int
    good_with_children: int
    good_with_other_dogs: int
    size: int
    good_alone: int
    
    @validator('energy_level', 'trainability', 'shedding_level', 
               'barking_level', 'playfulness', 'protectiveness',
               'good_with_children', 'good_with_other_dogs', 
               'good_alone')
    def validate_scale_1_5(cls, v):
        if not 1 <= v <= 5:
            raise ValueError('Debe estar entre 1 y 5')
        return v
    
    @validator('size')
    def validate_size(cls, v):
        if not 1 <= v <= 3:
            raise ValueError('Size debe ser 1 (pequeño), 2 (mediano) o 3 (grande)')
        return v
```

### 5.2 Mapeo desde Formulario HTML

**Formulario en `dog_home.html`**:
```html
<select name="energy_level" class="form-select" required>
    <option value="">Selecciona...</option>
    <option value="1">Muy baja (1)</option>
    <option value="2">Baja (2)</option>
    <option value="3">Moderada (3)</option>
    <option value="4">Alta (4)</option>
    <option value="5">Muy alta (5)</option>
</select>
```

**Procesamiento en FastAPI**:
```python
from fastapi import Form

@app.post("/recommend")
async def recommend_breed(
    energy_level: int = Form(...),
    trainability: int = Form(...),
    # ... resto de campos
):
    user_prefs = {
        'energy_level': energy_level,
        'trainability': trainability,
        # ... resto de características
    }
    
    recommendations = get_recommendation(user_prefs)
    return templates.TemplateResponse("dog_results.html", {
        "request": request,
        "breeds": recommendations
    })
```

---

## 6. Transformaciones y Normalizaciones

### 6.1 Normalización con StandardScaler

**Propósito**: Evitar que características con mayor magnitud dominen el cálculo de distancias en KNN.

**Proceso durante entrenamiento** (`train_dog_model.py`):
```python
from sklearn.preprocessing import StandardScaler

# 1. Cargar datos
df = pd.read_csv('data/dog_breeds_dataset.csv')
X = df[['energy_level', 'trainability', ...]]  # 10 features

# 2. Crear y entrenar scaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Guardar scaler
joblib.dump(scaler, 'models/dog_scaler.pkl')
```

**Transformación matemática**:
```
X_scaled = (X - mean) / std_deviation

Donde:
- mean = promedio de cada característica en el dataset
- std_deviation = desviación estándar de cada característica
```

**Ejemplo**:
```python
# Antes de normalizar
energy_level = [1, 2, 3, 4, 5]  # Rango: 1-5
mean = 3, std = 1.41

# Después de normalizar
energy_scaled = [-1.41, -0.71, 0, 0.71, 1.41]  # Media=0, Std=1
```

### 6.2 Aplicación en Predicción

```python
# Cargar scaler entrenado
scaler = joblib.load('models/dog_scaler.pkl')

# Entrada del usuario (sin normalizar)
user_input = [[4, 5, 2, 2, 4, 3, 5, 4, 2, 3]]

# Normalizar entrada
user_input_scaled = scaler.transform(user_input)

# Usar para predicción
model = joblib.load('models/dog_knn_model.pkl')
recommendations = model.kneighbors(user_input_scaled)
```

---

## 7. Estadísticas del Dataset

### 7.1 Distribución de Características

**Análisis exploratorio**:
```python
import pandas as pd

df = pd.read_csv('data/dog_breeds_dataset.csv')

# Estadísticas descriptivas
print(df.describe())
```

**Resultados**:
```
              energy  trainability  shedding  barking  playfulness
count         195.00        195.00    195.00   195.00       195.00
mean            3.42          3.68      3.15     3.22         3.71
std             0.89          0.94      1.12     0.98         0.85
min             1.00          1.00      1.00     1.00         1.00
25%             3.00          3.00      2.00     2.00         3.00
50%             3.00          4.00      3.00     3.00         4.00
75%             4.00          4.00      4.00     4.00         4.00
max             5.00          5.00      5.00     5.00         5.00
```

### 7.2 Distribución de Tamaños

```python
df['size'].value_counts()
```

**Resultados**:
```
size
2    98  (Mediano: 50%)
3    64  (Grande: 33%)
1    33  (Pequeño: 17%)
```

### 7.3 Top 10 Razas por Características

**Más energéticas**:
```python
df.nlargest(10, 'energy_level')[['breed', 'energy_level']]
```
```
Border Collie               5
Australian Shepherd         5
Jack Russell Terrier        5
Siberian Husky              5
Belgian Malinois            5
```

**Más fáciles de entrenar**:
```python
df.nlargest(10, 'trainability')[['breed', 'trainability']]
```
```
Golden Retriever            5
Labrador Retriever          5
German Shepherd             5
Poodle                      5
Border Collie               5
```

---

## 8. Mantenimiento del Dataset

### 8.1 Actualización de Datos

**Frecuencia recomendada**: Trimestral (el AKC actualiza razas ocasionalmente)

**Proceso**:
```bash
# 1. Descargar nueva versión de Kaggle
python3 download_dog_dataset.py

# 2. Adaptar al formato del proyecto
python3 adapt_kaggle_dataset.py

# 3. Reentrenar modelos
python3 train_dog_model.py

# 4. Verificar funcionamiento
./server.sh start
# Probar endpoint /recommend
```

### 8.2 Validación de Integridad

**Script de validación** (`validate_dataset.py`):
```python
import pandas as pd

def validate_dataset():
    df = pd.read_csv('data/dog_breeds_dataset.csv')
    
    # 1. Verificar número de razas
    assert len(df) == 195, f"Se esperan 195 razas, hay {len(df)}"
    
    # 2. Verificar columnas
    expected_cols = 11
    assert len(df.columns) == expected_cols
    
    # 3. Verificar no nulos
    assert df.isnull().sum().sum() == 0, "Hay valores nulos"
    
    # 4. Verificar rangos
    for col in df.columns[1:10]:  # Excluir 'breed'
        assert df[col].between(1, 5).all(), f"{col} fuera de rango"
    
    assert df['size'].between(1, 3).all(), "Size fuera de rango"
    
    print("✓ Dataset válido")

validate_dataset()
```

---

## 9. Backup y Versionado

### 9.1 Estrategia de Backup

**Ubicación de backups**: `data/backups/`

```bash
# Crear backup antes de actualizar
cp data/dog_breeds_dataset.csv \
   data/backups/dog_breeds_dataset_$(date +%Y%m%d).csv
```

### 9.2 Control de Versiones

**Git tracking**:
```bash
# Trackear cambios en dataset
git add data/dog_breeds_dataset.csv
git commit -m "Update dataset: Add 5 new AKC breeds"
git tag v1.1-dataset
```

---

## 10. Resolución de Problemas

### 10.1 Error: Dataset no encontrado

**Síntoma**:
```
FileNotFoundError: data/dog_breeds_dataset.csv not found
```

**Solución**:
```bash
python3 download_dog_dataset.py
python3 adapt_kaggle_dataset.py
```

### 10.2 Error: Kaggle authentication

**Síntoma**:
```
OSError: Could not find kaggle.json
```

**Solución**:
1. Ir a https://www.kaggle.com/account
2. Crear API token
3. Descargar `kaggle.json`
4. Colocar en `~/.kaggle/kaggle.json`
5. Dar permisos: `chmod 600 ~/.kaggle/kaggle.json`

### 10.3 Error: Columnas faltantes

**Síntoma**:
```
ValueError: Dataset tiene columnas faltantes
```

**Solución**:
```bash
# Readaptar dataset
python3 adapt_kaggle_dataset.py

# Verificar columnas
head -1 data/dog_breeds_dataset.csv
```

---

## Conclusión

El sistema de datos de Dog Breed AI se basa en:

1. **Fuente confiable**: Dataset oficial del American Kennel Club vía Kaggle
2. **Proceso automatizado**: Scripts de descarga y adaptación
3. **Transformaciones justificadas**: Cálculos de `size` y `good_alone`
4. **Validación robusta**: Pydantic + checks de integridad
5. **Normalización**: StandardScaler para mejores predicciones
6. **Mantenibilidad**: Scripts de backup y validación

El dataset final de **195 razas con 10 características** es el corazón del sistema de recomendación ML.
