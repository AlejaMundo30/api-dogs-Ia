# Documentación Completa - Dog Breed AI

## Sistema de Recomendación de Razas de Perros con Machine Learning

---

## Información del Proyecto

**Institución**: Tecnológico de Antioquia

**Integrantes**:
- Alejandra Orrego
- Stiven Aguirre
- Kevin

**Descripción**: Proyecto académico de Machine Learning que implementa un sistema de recomendación de razas de perros utilizando FastAPI, scikit-learn y análisis de datos con visualizaciones interactivas.

---

## Índice de Documentación

### 1. [Arquitectura del Sistema](01_ARQUITECTURA.md)
Diagrama y descripción detallada de la arquitectura completa del proyecto.

**Contenido**:
- Diagrama de componentes (FastAPI, ML, Datos)
- Flujo de datos completo
- Estructura de carpetas
- Interacción entre módulos
- Entorno de ejecución

**Audiencia**: Desarrolladores, arquitectos de software

---

### 2. [Manual de Instalación y Despliegue](02_MANUAL_INSTALACION.md)
Guía paso a paso para instalar y configurar el proyecto.

**Contenido**:
- Requisitos del sistema
- Versiones de Python y librerías
- Creación de entorno virtual
- Instalación de dependencias
- Configuración del proyecto
- Ejecución del servidor FastAPI
- Scripts de automatización (install.sh, server.sh)

**Audiencia**: DevOps, desarrolladores nuevos en el proyecto

---

### 3. [Manual de Usuario de la API](03_MANUAL_USUARIO.md)
Guía práctica para consumir la API REST.

**Contenido**:
- Descripción de endpoints
- Ejemplos de peticiones y respuestas JSON
- Instrucciones con curl, Postman, Swagger UI
- Interpretación de resultados
- Casos de uso comunes
- Troubleshooting

**Audiencia**: Usuarios de la API, frontend developers, testers

---

### 4. [Documentación Técnica](04_DOCUMENTACION_TECNICA.md)
Explicación detallada del funcionamiento interno del sistema.

**Contenido**:
- Estructura del código
- Librerías utilizadas y justificación
- Descripción de modelos ML (KNN, Random Forest, KMeans)
- Parámetros de modelos
- Decisiones técnicas (FastAPI vs Flask, etc.)
- Optimizaciones implementadas
- Seguridad y escalabilidad

**Audiencia**: Desarrolladores senior, mantenedores del código

---

### 5. [Manual de Preparación de Datos](05_MANUAL_DATOS.md)
Especificación completa sobre datos del proyecto.

**Contenido**:
- Fuente del dataset (Kaggle - AKC)
- Formato y estructura de datos
- Proceso de descarga y adaptación
- Carga de datasets
- Estructura esperada de entrada
- Transformaciones y normalizaciones (StandardScaler)
- Características derivadas (size, good_alone)
- Ubicación de archivos

**Audiencia**: Data scientists, analistas, desarrolladores de ML

---

## Inicio Rápido

### Instalación en 2 pasos

```bash
# 1. Ejecutar instalador automático
./install.sh

# 2. Iniciar servidor
./server.sh start
```

### Acceso a la aplicación

- **Página de inicio**: http://localhost:8000
- **Catálogo de razas**: http://localhost:8000/breeds
- **API Docs (Swagger)**: http://localhost:8000/docs
- **API Docs (ReDoc)**: http://localhost:8000/redoc

---

## Resumen del Proyecto

### Descripción
Sistema inteligente que recomienda razas de perros basándose en las preferencias del usuario utilizando algoritmos de Machine Learning.

### Tecnologías Principales
- **Backend**: FastAPI (Python 3.9+)
- **ML**: scikit-learn (KNN, Random Forest, KMeans)
- **Datos**: Pandas, 195 razas AKC (Kaggle)
- **Frontend**: HTML5, Bootstrap 5, JavaScript

### Características Clave
- 195 razas del American Kennel Club
- 10 características comportamentales por raza
- 3 modelos ML entrenados (KNN, RF, KMeans)
- API REST con documentación automática
- Interfaz web interactiva
- Sistema de scoring de compatibilidad (0-100)

---

## 📂 Estructura de Documentación

```
docs/
├── README.md                        # Este archivo (índice)
├── 01_ARQUITECTURA.md               # Arquitectura del sistema
├── 02_MANUAL_INSTALACION.md         # Instalación y despliegue
├── 03_MANUAL_USUARIO.md             # Uso de la API
├── 04_DOCUMENTACION_TECNICA.md      # Detalles técnicos
└── 05_MANUAL_DATOS.md               # Preparación de datos
```

---

## 🎯 Objetivo del Proyecto

El proyecto final consiste en diseñar, documentar y desplegar de forma manual una solución de Machine Learning que exponga un modelo predictivo a través de una API desarrollada con FastAPI.

### Componentes Integrados

1. **Arquitectura de la solución** ✅
   - Diagrama detallado en `01_ARQUITECTURA.md`
   - Muestra conexión entre modelo ML, API, datos y entorno

2. **Manual de instalación o despliegue** ✅
   - Guía paso a paso en `02_MANUAL_INSTALACION.md`
   - Scripts automatizados: `install.sh`, `server.sh`
   - Requisitos, versiones, configuración completa

3. **Manual de usuario** ✅
   - Guía práctica en `03_MANUAL_USUARIO.md`
   - Endpoints, ejemplos JSON, curl/Postman/Swagger
   - Interpretación de resultados

4. **Documentación técnica** ✅
   - Funcionamiento interno en `04_DOCUMENTACION_TECNICA.md`
   - Estructura código, librerías, modelos ML
   - Justificación de decisiones técnicas

5. **Manual de datos (preparación de datos)** ✅
   - Especificación completa en `05_MANUAL_DATOS.md`
   - Fuente (Kaggle), formato, carga, transformaciones
   - Ubicación archivos, normalizaciones

---

## 🔗 Enlaces Útiles

### Recursos Externos
- **Dataset**: [Kaggle - Dog Breeds Dataset](https://www.kaggle.com/datasets/sujaykapadnis/dog-breeds)
- **FastAPI Docs**: https://fastapi.tiangolo.com/
- **scikit-learn**: https://scikit-learn.org/
- **American Kennel Club**: https://www.akc.org/

### Repositorio
- **GitHub**: https://github.com/AlejaMundo30/api-dogs-Ia

---

## Consejos para Navegación

### Si eres nuevo en el proyecto:
1. Lee primero `02_MANUAL_INSTALACION.md` para configurar todo
2. Luego `03_MANUAL_USUARIO.md` para aprender a usar la API
3. Consulta `01_ARQUITECTURA.md` para entender la estructura

### Si eres desarrollador:
1. Revisa `04_DOCUMENTACION_TECNICA.md` para detalles del código
2. Consulta `05_MANUAL_DATOS.md` para entender los datos
3. Usa `01_ARQUITECTURA.md` como referencia del diseño

### Si trabajas con datos:
1. Empieza con `05_MANUAL_DATOS.md`
2. Revisa `04_DOCUMENTACION_TECNICA.md` para modelos ML
3. Consulta `03_MANUAL_USUARIO.md` para ver la API

---

## 📞 Soporte

Para preguntas o problemas:
1. Consulta la sección de Troubleshooting en cada manual
2. Revisa los logs del servidor
3. Abre un issue en GitHub

---

## Licencia

Dataset bajo licencia de Kaggle - Fuente: American Kennel Club

---

**Última actualización**: Noviembre 2025  
**Versión del proyecto**: 1.0  
**Python requerido**: 3.9+
