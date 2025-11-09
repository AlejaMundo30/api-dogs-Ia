from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from controllers.iris_controller import router as iris_router
from controllers.dog_controller import router as dog_router

# Crear la instancia de FastAPI
app = FastAPI(title="🌸🐕 Predictor de Iris y Recomendador de Razas de Perros")

# Montar recursos estáticos
app.mount("/css", StaticFiles(directory=Path(__file__).resolve().parent / "static/css"), name="css")
app.mount("/js", StaticFiles(directory=Path(__file__).resolve().parent / "static/js"), name="js")
app.mount("/images", StaticFiles(directory=Path(__file__).resolve().parent / "static/images"), name="images")
app.mount("/fonts", StaticFiles(directory=Path(__file__).resolve().parent / "static/fonts"), name="fonts")
app.mount("/videos", StaticFiles(directory=Path(__file__).resolve().parent / "static/videos"), name="videos")

# Registrar las rutas
app.include_router(iris_router, prefix="/iris", tags=["iris"])
app.include_router(dog_router, prefix="/dogs", tags=["dogs"])

@app.get("/")
async def root():
    """Página de inicio con opciones"""
    from fastapi.responses import HTMLResponse
    
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🌸🐕 ML Applications</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
            }
            .app-card {
                border-radius: 20px;
                transition: all 0.3s ease;
                background: rgba(255,255,255,0.95);
                backdrop-filter: blur(10px);
            }
            .app-card:hover {
                transform: translateY(-10px);
                box-shadow: 0 20px 40px rgba(0,0,0,0.2);
            }
        </style>
    </head>
    <body>
        <div class="container py-5">
            <div class="row justify-content-center">
                <div class="col-md-10">
                    <div class="text-center mb-5">
                        <h1 class="text-white display-4 fw-bold mb-3">🤖 Aplicaciones de Machine Learning</h1>
                        <p class="text-white-50 fs-5">Explora nuestras aplicaciones inteligentes</p>
                    </div>
                    
                    <div class="row g-4">
                        <!-- Aplicación Iris -->
                        <div class="col-md-6">
                            <div class="app-card card h-100 p-4 text-center">
                                <div class="card-body d-flex flex-column">
                                    <div class="mb-4">
                                        <div style="font-size: 4rem;">🌸</div>
                                    </div>
                                    <h3 class="card-title text-primary mb-3">Clasificador de Iris</h3>
                                    <p class="card-text mb-4">
                                        Predice la especie de flor Iris basándose en las medidas de sus pétalos y sépalos.
                                        Utiliza algoritmos de clustering y clasificación.
                                    </p>
                                    <div class="mt-auto">
                                        <a href="/iris/" class="btn btn-primary btn-lg">
                                            🌺 Clasificar Iris
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        
                        <!-- Aplicación Perros -->
                        <div class="col-md-6">
                            <div class="app-card card h-100 p-4 text-center">
                                <div class="card-body d-flex flex-column">
                                    <div class="mb-4">
                                        <div style="font-size: 4rem;">🐕</div>
                                    </div>
                                    <h3 class="card-title text-primary mb-3">Recomendador de Razas</h3>
                                    <p class="card-text mb-4">
                                        Encuentra la raza de perro perfecta para ti basándose en tus preferencias y estilo de vida.
                                        Sistema de recomendación inteligente.
                                    </p>
                                    <div class="mt-auto">
                                        <a href="/dogs/" class="btn btn-primary btn-lg">
                                            🐾 Encontrar mi Raza
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="text-center mt-5">
                        <p class="text-white-50">
                            Powered by FastAPI + Scikit-learn + Machine Learning
                        </p>
                    </div>
                </div>
            </div>
        </div>
        
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
    
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)