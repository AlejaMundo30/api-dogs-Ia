import joblib
import numpy as np
import pandas as pd
import json
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from io import BytesIO
from PIL import Image
import base64
from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os

# Crear el enrutador para las peticiones
router = APIRouter()

# Inicializar el objeto Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Cargar modelos y datos
try:
    scaler = joblib.load('models/dog_scaler.pkl')
    knn_model = joblib.load('models/dog_knn_model.pkl')
    kmeans_model = joblib.load('models/dog_kmeans_model.pkl')
    
    with open('models/breed_info.json', 'r', encoding='utf-8') as f:
        breed_info = json.load(f)
    
    # Cargar dataset original
    df = pd.read_csv('data/dog_breeds_dataset.csv')
    
    print("✓ Modelos de perros cargados exitosamente")
except Exception as e:
    print(f"Error cargando modelos: {e}")

def recommend_breed(user_preferences):
    """Recomienda razas basadas en las preferencias del usuario"""
    try:
        # Normalizar las preferencias del usuario
        user_scaled = scaler.transform([user_preferences])
        
        # Usar KNN para encontrar razas similares
        distances, indices = knn_model.kneighbors(user_scaled, n_neighbors=5)
        
        # Obtener las razas recomendadas
        recommended_breeds = []
        for idx in indices[0]:
            breed_name = df.iloc[idx]['breed']
            similarity = 1 / (1 + distances[0][len(recommended_breeds)])  # Convertir distancia a similitud
            recommended_breeds.append({
                'breed': breed_name,
                'similarity': similarity,
                'characteristics': df.iloc[idx].to_dict()
            })
        
        return recommended_breeds
    except Exception as e:
        print(f"Error en recomendación: {e}")
        return []

def find_similar_breeds(user_preferences, top_n=5):
    """Encuentra razas similares usando similitud coseno"""
    try:
        # Normalizar preferencias del usuario
        user_scaled = scaler.transform([user_preferences])
        
        # Normalizar todo el dataset
        x_scaled = scaler.transform(df.drop('breed', axis=1))
        
        # Calcular similitud coseno
        similarities = cosine_similarity(user_scaled, x_scaled)[0]
        
        # Obtener los indices más similares
        similar_indices = similarities.argsort()[-top_n:][::-1]
        
        results = []
        for idx in similar_indices:
            breed_data = df.iloc[idx]
            results.append({
                'breed': breed_data['breed'],
                'similarity': similarities[idx],
                'characteristics': breed_data.to_dict()
            })
        
        return results
    except Exception as e:
        print(f"Error buscando similares: {e}")
        return []

def generate_comparison_plot(user_preferences, recommended_breeds):
    """Genera un gráfico comparativo entre el perfil del usuario y las razas recomendadas"""
    try:
        # Preparar datos para el gráfico
        features = breed_info['features']
        
        # Crear el gráfico
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Gráfico de radar/polar sería ideal, pero usaremos barras por simplicidad
        x_pos = np.arange(len(features))
        
        # Perfil del usuario
        ax.bar(x_pos - 0.2, user_preferences, 0.4, label='Tu Perfil', alpha=0.7, color='skyblue')
        
        # Raza más recomendada
        if recommended_breeds:
            best_breed = recommended_breeds[0]
            breed_values = [best_breed['characteristics'][feature] for feature in features]
            ax.bar(x_pos + 0.2, breed_values, 0.4, 
                  label=f"{best_breed['breed']}", alpha=0.7, color='lightcoral')
        
        # Configurar el gráfico
        ax.set_xlabel('Características')
        ax.set_ylabel('Puntuación (1-5)')
        ax.set_title('Comparación de Perfil: Tu vs Raza Recomendada')
        ax.set_xticks(x_pos)
        ax.set_xticklabels([f.replace('_', '\n') for f in features], rotation=45, ha='right')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Guardar como imagen base64
        buf = BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format="png", dpi=150, bbox_inches='tight')
        buf.seek(0)
        img_base64 = base64.b64encode(buf.getvalue()).decode("utf-8")
        
        plt.close(fig)
        return img_base64
    
    except Exception as e:
        print(f"Error generando gráfico: {e}")
        return None

@router.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    """Página de inicio del clasificador"""
    return templates.TemplateResponse("dog_home.html", {"request": request})

@router.get("/home", response_class=HTMLResponse)
async def home_page_redirect(request: Request):
    """Redirección alternativa a la página de inicio"""
    return templates.TemplateResponse("dog_home.html", {"request": request})

@router.get("/", response_class=HTMLResponse)
async def dog_form(request: Request):
    """Renderiza el formulario para encontrar la raza perfecta"""
    return templates.TemplateResponse("dog_form.html", {
        "request": request,
        "features": breed_info['features'],
        "descriptions": breed_info['feature_descriptions']
    })

@router.get("/form", response_class=HTMLResponse)
async def dog_form_step(request: Request):
    """Formulario paso a paso con nuevo diseño"""
    return templates.TemplateResponse("dog_form_new.html", {
        "request": request,
        "features": breed_info['features'],
        "descriptions": breed_info['feature_descriptions']
    })

@router.post("/recommend", response_class=HTMLResponse)
async def recommend_dogs(
    request: Request,
    size: int = Form(...),
    energy_level: int = Form(...),
    trainability: int = Form(...),
    good_with_kids: int = Form(...),
    exercise_needs: int = Form(...),
    barking_tendency: int = Form(...),
    grooming_needs: int = Form(...),
    apartment_friendly: int = Form(...),
    good_alone: int = Form(...),
    watchdog_ability: int = Form(...)
):
    """Recibe las preferencias y devuelve recomendaciones de razas"""
    
    # Recopilar preferencias del usuario
    user_preferences = [
        size, energy_level, trainability, good_with_kids, exercise_needs,
        barking_tendency, grooming_needs, apartment_friendly, good_alone, watchdog_ability
    ]
    
    # Obtener recomendaciones
    recommendations = find_similar_breeds(user_preferences, top_n=5)
    
    # Generar gráfico comparativo
    comparison_plot = generate_comparison_plot(user_preferences, recommendations)
    
    return templates.TemplateResponse("dog_results.html", {
        "request": request,
        "recommendations": recommendations,
        "user_preferences": dict(zip(breed_info['features'], user_preferences)),
        "feature_descriptions": breed_info['feature_descriptions'],
        "comparison_plot": comparison_plot
    })

@router.get("/breeds", response_class=HTMLResponse)
async def list_breeds(request: Request):
    """Lista todas las razas disponibles"""
    breeds_data = df.to_dict('records')
    return templates.TemplateResponse("dog_breeds.html", {
        "request": request,
        "breeds": breeds_data,
        "feature_descriptions": breed_info['feature_descriptions']
    })