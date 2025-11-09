# Arquitectura del Sistema - Dog Breed AI

**Proyecto**: Sistema de Recomendación de Razas de Perros con Machine Learning  
**Institución**: Tecnológico de Antioquia  
**Autores**: Alejandra Orrego, Stiven Aguirre, Kevin

---

## Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────────┐
│                         USUARIO FINAL                            │
│                    (Navegador Web / API Client)                  │
└────────────────┬────────────────────────────────────────────────┘
                 │ HTTP Requests
                 │ (GET, POST)
                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FASTAPI APPLICATION                         │
│                         (main.py)                                │
│                                                                   │
│  Endpoints:                                                       │
│  • GET  /              → Home Page                               │
│  • GET  /breeds        → Catálogo de razas                       │
│  • GET  /analytics     → Dashboard de análisis y visualizaciones │
│  • POST /recommend     → Recomendación ML                        │
│  • GET  /docs          → Swagger UI                              │
│  • GET  /redoc         → ReDoc                                   │
└────────────┬────────────────────────────────┬───────────────────┘
             │                                │
             │ Templates                      │ Business Logic
             ▼                                ▼
┌─────────────────────┐        ┌──────────────────────────────────┐
│  JINJA2 TEMPLATES   │        │   CONTROLLERS                    │
│  (templates/)       │        ├──────────────────────────────────┤
│                     │        │  DOG CONTROLLER                  │
│  • dog_home.html    │        │  (controllers/dog_controller.py) │
│  • dog_breeds.html  │        │                                  │
│  • dog_results.html │        │  • get_recommendation()          │
│  • dog_analytics.html│       │  • load_models()                 │
│  • index.html       │        │  • calculate_scores()            │
│                     │        │  • feature_engineering()         │
│                     │        ├──────────────────────────────────┤
│                     │        │  ANALYTICS CONTROLLER            │
│                     │        │  (controllers/analytics_controller.py)│
│                     │        │                                  │
│                     │        │  • generate_all_charts()         │
│                     │        │  • generate_pair_plot()          │
│                     │        │  • generate_correlation_heatmap()│
│                     │        │  • generate_feature_distributions()│
└─────────────────────┘        └────────┬─────────────────────────┘
                                        │
                                        │ Carga modelos y datos
                                        ▼
┌─────────────────────────────────────────────────────────────────┐
│                    CAPA DE DATOS Y MODELOS                       │
├─────────────────────────────────┬───────────────────────────────┤
│   MODELOS ML (models/)          │   DATASET (data/)             │
│                                 │                                │
│  • dog_knn_model.pkl            │  • dog_breeds_dataset.csv     │
│    - K-Nearest Neighbors        │    (195 razas AKC)            │
│    - Recomendación por          │                                │
│      similitud                  │  Características:             │
│                                 │  • energy_level               │
│  • dog_random_forest.pkl        │  • trainability               │
│    - Random Forest Classifier   │  • shedding_level             │
│    - Clasificación avanzada     │  • barking_level              │
│                                 │  • playfulness                │
│  • dog_kmeans_model.pkl         │  • protectiveness             │
│    - KMeans Clustering          │  • good_with_children         │
│    - Agrupación de razas        │  • good_with_other_dogs       │
│                                 │  • size (calculado)           │
│  • dog_scaler.pkl               │  • good_alone (calculado)     │
│    - StandardScaler             │                                │
│    - Normalización features     │                                │
└─────────────────────────────────┴───────────────────────────────┘
                                        ▲
                                        │ Descarga y adaptación
                                        │
┌─────────────────────────────────────────────────────────────────┐
│                   FUENTE EXTERNA - KAGGLE                        │
│                                                                   │
│  Dataset: sujaykapadnis/dog-breeds                               │
│  • 195 razas del American Kennel Club                           │
│  • 14 características originales                                │
│  • Descarga: download_dog_dataset.py                            │
│  • Adaptación: adapt_kaggle_dataset.py                          │
└─────────────────────────────────────────────────────────────────┘
```

## Flujo de Datos

### 1. **Inicialización del Sistema**
```
[Kaggle] → download_dog_dataset.py → [breed_traits.csv]
         → adapt_kaggle_dataset.py → [dog_breeds_dataset.csv]
         → train_dog_model.py → [Modelos ML .pkl]
```

### 2. **Flujo de Recomendación**
```
Usuario → FastAPI (/recommend) → dog_controller.py
                                      ↓
                          Cargar modelos y dataset
                                      ↓
                          Feature engineering
                          (crear características derivadas)
                                      ↓
                          Normalizar con StandardScaler
                                      ↓
                          Predecir con KNN/RandomForest
                                      ↓
                          Ranking de razas (top 5)
                                      ↓
                          Renderizar dog_results.html
                                      ↓
                          ← Respuesta HTML al usuario
```

### 3. **Flujo de Catálogo**
```
Usuario → FastAPI (/breeds) → dog_controller.py
                                      ↓
                          Cargar dog_breeds_dataset.csv
                                      ↓
                          Convertir a lista de diccionarios
                                      ↓
                          Renderizar dog_breeds.html
                          (con JavaScript para filtros)
                                      ↓
                          ← Respuesta HTML con 195 razas
```

## Componentes del Sistema

### **1. Capa de Presentación**
- **FastAPI**: Framework web asíncrono
- **Jinja2**: Motor de templates para HTML dinámico
- **Bootstrap 5**: Framework CSS para UI responsive
- **JavaScript**: Filtros y búsqueda en tiempo real

### **2. Capa de Lógica de Negocio**
- **dog_controller.py**: Controlador principal
  - Gestión de modelos ML
  - Cálculo de recomendaciones
  - Procesamiento de formularios

### **3. Capa de Machine Learning**
- **KNN**: Encuentra razas similares por proximidad
- **Random Forest**: Clasifica preferencias complejas
- **KMeans**: Agrupa razas con características similares
- **StandardScaler**: Normaliza features (media=0, std=1)

### **4. Capa de Datos**
- **CSV Dataset**: 195 razas con 10 características
- **Kaggle Hub**: Descarga automática del dataset oficial
- **Pandas**: Manipulación y transformación de datos

## Tecnologías Utilizadas

| Componente | Tecnología | Versión | Propósito |
|------------|------------|---------|-----------|
| Web Framework | FastAPI | 0.104+ | API REST y web server |
| ASGI Server | Uvicorn | 0.24+ | Servidor de aplicación |
| ML Framework | scikit-learn | 1.3+ | Modelos predictivos |
| Data Processing | Pandas | 2.1+ | Manipulación de datos |
| Templates | Jinja2 | 3.1+ | Renderizado HTML |
| Dataset Source | kagglehub | 0.2+ | Descarga de Kaggle |
| Serialization | joblib | 1.3+ | Persistencia de modelos |

## Entorno de Ejecución

### **Desarrollo**
```
Python 3.9+ → .venv (virtual environment)
              ↓
         pip install -r requirements.txt
              ↓
         uvicorn main:app --reload
         (Hot reload activado)
```

### **Producción** (recomendado)
```
Python 3.9+ → .venv
              ↓
         pip install -r requirements.txt
              ↓
         uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
         (Multi-proceso para escalabilidad)
```

## Escalabilidad y Rendimiento

### **Optimizaciones Implementadas**
1. **Carga única de modelos**: Los modelos .pkl se cargan una sola vez al iniciar
2. **Pandas eficiente**: Uso de vectorización en lugar de loops
3. **FastAPI async**: Permite múltiples requests concurrentes
4. **Caching de templates**: Jinja2 cachea templates compilados

### **Posibles Mejoras Futuras**
- Redis para cache de recomendaciones frecuentes
- PostgreSQL para datos de usuarios y favoritos
- Docker para containerización
- Nginx como reverse proxy
- Prometheus + Grafana para monitoreo

## Seguridad

- **Validación de entrada**: Pydantic models para validar requests
- **CORS configurado**: Solo orígenes permitidos
- **Sin datos sensibles**: No se almacenan datos personales
- **Rate limiting**: (implementable con slowapi)

## Diagrama de Despliegue

```
┌──────────────────────────────────────┐
│         Sistema Operativo             │
│      (macOS / Linux / Windows)        │
│                                       │
│  ┌─────────────────────────────────┐ │
│  │   Python Virtual Environment    │ │
│  │          (.venv)                │ │
│  │                                 │ │
│  │  ┌───────────────────────────┐ │ │
│  │  │   Uvicorn ASGI Server     │ │ │
│  │  │   (puerto 8000)           │ │ │
│  │  │                           │ │ │
│  │  │  ┌─────────────────────┐ │ │ │
│  │  │  │  FastAPI App        │ │ │ │
│  │  │  │  (main.py)          │ │ │ │
│  │  │  │                     │ │ │ │
│  │  │  │  ┌───────────────┐ │ │ │ │
│  │  │  │  │ Controllers   │ │ │ │ │
│  │  │  │  │ Templates     │ │ │ │ │
│  │  │  │  │ Static files  │ │ │ │ │
│  │  │  │  │ ML Models     │ │ │ │ │
│  │  │  │  │ Dataset       │ │ │ │ │
│  │  │  │  └───────────────┘ │ │ │ │
│  │  │  └─────────────────────┘ │ │ │
│  │  └───────────────────────────┘ │ │
│  └─────────────────────────────────┘ │
└──────────────────────────────────────┘
         ▲
         │ HTTP/HTTPS
         │
    [Usuarios/Clientes]
```

---

**Conclusión**: El sistema sigue una arquitectura MVC (Model-View-Controller) adaptada para Machine Learning, con separación clara de responsabilidades entre presentación, lógica de negocio y datos.
