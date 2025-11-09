from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from controllers.dog_controller import router as dog_router

# Crear la instancia de FastAPI
app = FastAPI(title="🐕 Dog Breed AI - Clasificador Inteligente")

# Montar cada carpeta de recursos estáticos de forma independiente
app.mount("/css", StaticFiles(directory=Path(__file__).resolve().parent / "static/css"), name="css")
app.mount("/js", StaticFiles(directory=Path(__file__).resolve().parent / "static/js"), name="js")
app.mount("/images", StaticFiles(directory=Path(__file__).resolve().parent / "static/images"), name="images")
app.mount("/fonts", StaticFiles(directory=Path(__file__).resolve().parent / "static/fonts"), name="fonts")
app.mount("/videos", StaticFiles(directory=Path(__file__).resolve().parent / "static/videos"), name="videos")

# Registrar las rutas del controlador de perros
app.include_router(dog_router, prefix="", tags=["dogs"])

# La página de inicio se maneja directamente en el controlador

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse("static/favicon.ico")



#uvicorn app.main:app --reload