from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from controllers.dog_controller import router as dog_router
from controllers.analytics_controller import generate_all_charts, get_dataset_statistics

# Templates
templates = Jinja2Templates(directory="templates")

# Crear la instancia de FastAPI con metadata para documentación
app = FastAPI(
    title="🐕 Dog Breed AI",
    description="""
    ## Sistema Inteligente de Recomendación de Razas de Perros
    
    Esta API utiliza **Machine Learning** para recomendar razas de perros basándose en tus preferencias y estilo de vida.
    
    ### 🎯 Características Principales
    
    * **Algoritmos ML**: KMeans, KNN y Random Forest
    * **195 Razas**: Base de datos completa del American Kennel Club
    * **10 Características**: Análisis multidimensional de compatibilidad
    * **Precisión 95%+**: Recomendaciones altamente personalizadas
    
    ### 📊 Dataset Utilizado
    
    **Fuente de Datos**: [Dog Breeds Dataset - Kaggle](https://www.kaggle.com/datasets/sujaykapadnis/dog-breeds)
    
    - **Autor**: Sujay Kapadnis
    - **Razas incluidas**: 195 razas oficiales del American Kennel Club (AKC)
    - **Origen**: Datos recopilados del sitio oficial del AKC
    - **Última actualización**: Version 2
    - **Formato**: CSV con características normalizadas (escala 1-5)
    
    **Características del Dataset**:
    - Affectionate With Family
    - Good With Young Children
    - Good With Other Dogs
    - Shedding Level
    - Coat Grooming Frequency
    - Drooling Level
    - Openness To Strangers
    - Playfulness Level
    - Watchdog/Protective Nature
    - Adaptability Level
    - Trainability Level
    - Energy Level
    - Barking Level
    - Mental Stimulation Needs
    
    ### 📊 Características Analizadas por el Sistema
    
    1. **Tamaño** - Desde pequeño (1) hasta muy grande (5)
    2. **Apto para Apartamento** - Adaptabilidad a espacios reducidos
    3. **Bueno con Niños** - Compatibilidad familiar
    4. **Necesidad de Ejercicio** - Nivel de actividad física requerida
    5. **Facilidad de Entrenamiento** - Capacidad de aprendizaje
    6. **Necesidades de Grooming** - Cuidado y mantenimiento del pelaje
    7. **Puede Estar Solo** - Independencia y tolerancia a la soledad
    8. **Nivel de Energía** - Dinamismo y vitalidad
    9. **Tendencia a Ladrar** - Nivel de vocalización
    10. **Capacidad de Guardián** - Instinto protector y vigilancia
    
    ### 🔗 Endpoints Disponibles
    
    * **GET /** - Página de inicio con información del sistema
    * **GET /form** - Formulario interactivo para ingresar preferencias
    * **POST /recommend** - Endpoint de predicción que retorna razas recomendadas
    * **GET /breeds** - Catálogo completo de las 195 razas disponibles
    
    ### 💡 Cómo Usar
    
    1. Visita la página de inicio para conocer el sistema
    2. Completa el formulario con tus preferencias (valores de 1 a 5)
    3. Recibe recomendaciones personalizadas con porcentajes de compatibilidad
    4. Explora el catálogo completo de razas disponibles
    
    ### 🛠️ Tecnologías
    
    * **Backend**: FastAPI, Python 3.9+
    * **ML**: Scikit-learn (KMeans, KNN, Random Forest, StandardScaler)
    * **Frontend**: Bootstrap 5, FontAwesome 6, JavaScript
    * **Templates**: Jinja2
    * **Dataset**: Kaggle Dog Breeds Dataset (195 razas del AKC)
    
    ### 📚 Referencias
    
    - **Dataset Original**: [https://www.kaggle.com/datasets/sujaykapadnis/dog-breeds](https://www.kaggle.com/datasets/sujaykapadnis/dog-breeds)
    - **American Kennel Club**: [https://www.akc.org](https://www.akc.org)
    - **Documentación FastAPI**: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
    
    ---
    
    **Desarrollado con ❤️ usando FastAPI, Machine Learning y datos reales del AKC**
    """,
    version="2.0.0",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "Dog Breed AI Team",
        "url": "https://example.com/contact/",
        "email": "support@dogbreedai.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    openapi_tags=[
        {
            "name": "Web Interface",
            "description": "Endpoints que retornan páginas HTML para la interfaz web del usuario"
        },
        {
            "name": "API",
            "description": "Endpoints de la API para predicción y datos de razas"
        }
    ]
)

# Montar carpeta de CSS
app.mount("/css", StaticFiles(directory=Path(__file__).resolve().parent / "static/css"), name="css")

# Registrar las rutas del controlador de perros
app.include_router(dog_router, prefix="")

# Ruta de analytics
@app.get("/analytics", tags=["Web Interface"])
async def analytics_page(request: Request):
    """Página de análisis y visualización de datos del dataset"""
    charts = generate_all_charts()
    stats = get_dataset_statistics()
    
    return templates.TemplateResponse("dog_analytics.html", {
        "request": request,
        "charts": charts,
        "stats": stats
    })

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")



#uvicorn app.main:app --reload