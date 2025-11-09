# Manual de Usuario - Dog Breed AI API

**Proyecto**: Sistema de Recomendación de Razas de Perros con Machine Learning  
**Institución**: Tecnológico de Antioquia  
**Autores**: Alejandra Orrego, Stiven Aguirre, Kevin

---

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Acceso a la API](#acceso-a-la-api)
3. [Endpoints Disponibles](#endpoints-disponibles)
4. [Ejemplos de Uso](#ejemplos-de-uso)
5. [Pruebas con Diferentes Herramientas](#pruebas-con-diferentes-herramientas)
6. [Interpretación de Resultados](#interpretación-de-resultados)

---

## Introducción

Dog Breed AI es un sistema de recomendación de razas de perros basado en Machine Learning que analiza tus preferencias y estilo de vida para sugerirte las razas más compatibles.

### ¿Qué Puede Hacer?

- **Buscar la raza perfecta** según tus necesidades
- **Explorar 195 razas** del American Kennel Club
- **Obtener recomendaciones personalizadas** con porcentajes de compatibilidad
- **Acceso web y API REST** para integración en otras aplicaciones

---

## Acceso a la API

### URLs de Acceso

Una vez iniciado el servidor (`./server.sh start`), la API estará disponible en:

| Recurso | URL | Descripción |
|---------|-----|-------------|
| **Home** | http://localhost:8000 | Página de inicio |
| **Formulario** | http://localhost:8000/form | Formulario interactivo |
| **Catálogo** | http://localhost:8000/breeds | Ver 195 razas |
| **Analytics** | http://localhost:8000/analytics | Análisis y visualizaciones del dataset |
| **Swagger UI** | http://localhost:8000/docs | Documentación interactiva |
| **ReDoc** | http://localhost:8000/redoc | Documentación alternativa |

### Autenticación

****No requiere autenticación** - La API es de acceso público

---

## Endpoints Disponibles

### 1. GET / - Página de Inicio

**Descripción**: Página principal con información del sistema

**URL**: `http://localhost:8000/`

**Método**: GET

**Respuesta**: HTML con información del proyecto

---

### 2. GET /form - Formulario de Preferencias

**Descripción**: Formulario interactivo para ingresar tus preferencias

**URL**: `http://localhost:8000/form`

**Método**: GET

**Respuesta**: HTML con formulario de 10 campos

**Campos del Formulario**:

| Campo | Nombre | Rango | Descripción |
|-------|--------|-------|-------------|
| `size` | Tamaño | 1-5 | 1=Muy pequeño, 5=Gigante |
| `good_with_children` | Bueno con niños | 1-5 | 1=No recomendado, 5=Excelente |
| `good_with_other_dogs` | Bueno con otros perros | 1-5 | 1=No compatible, 5=Muy sociable |
| `shedding_level` | Nivel de muda | 1-5 | 1=Casi nada, 5=Mucho |
| `grooming_level` | Necesidad de aseo | 1-5 | 1=Bajo, 5=Alto mantenimiento |
| `trainability` | Facilidad de entrenamiento | 1-5 | 1=Difícil, 5=Muy fácil |
| `barking_level` | Nivel de ladridos | 1-5 | 1=Silencioso, 5=Muy vocal |
| `energy_level` | Nivel de energía | 1-5 | 1=Tranquilo, 5=Muy activo |
| `protectiveness` | Capacidad de guardián | 1-5 | 1=Nula, 5=Excelente guardián |
| `playfulness` | Nivel de juego | 1-5 | 1=Calmado, 5=Muy juguetón |

---

### 3. POST /recommend - Obtener Recomendaciones

**Descripción**: Endpoint principal que procesa tus preferencias y retorna razas recomendadas

**URL**: `http://localhost:8000/recommend`

**Método**: POST

**Content-Type**: `application/x-www-form-urlencoded`

**Parámetros del Body**:

```json
{
  "size": 3,
  "good_with_children": 5,
  "good_with_other_dogs": 4,
  "shedding_level": 2,
  "grooming_level": 2,
  "trainability": 4,
  "barking_level": 2,
  "energy_level": 3,
  "protectiveness": 4,
  "playfulness": 4
}
```

**Respuesta**: HTML con las Top 5 razas recomendadas

---

### 4. GET /breeds - Catálogo Completo

**Descripción**: Visualiza las 195 razas disponibles con búsqueda y filtros

**URL**: `http://localhost:8000/breeds`

**Método**: GET

**Funcionalidades**:
- Búsqueda por nombre de raza
- Filtro por tamaño (pequeño/mediano/grande)
- Vista de todas las características
- Imágenes de cada raza

---

### 5. GET /analytics - Dashboard de Análisis

**Descripción**: Panel de visualización con análisis exploratorio del dataset

**URL**: `http://localhost:8000/analytics`

**Método**: GET

**Visualizaciones Incluidas**:

#### Estadísticas Generales
- **195 Razas**: Total de razas en el dataset
- **10 Features**: Características analizadas
- **7 Gráficos**: Visualizaciones interactivas

#### Gráficos Disponibles

1. **Distribución de Tamaños**
   - Gráfico de pastel mostrando proporción de razas por tamaño (1-5)
   - Identifica balance entre razas pequeñas, medianas y grandes

2. **Pair Plot - Matriz de Relaciones**
   - Similar al análisis del dataset Iris
   - Muestra todas las combinaciones entre 4 características principales:
     * `energy_level` (Nivel de energía)
     * `trainability` (Facilidad de entrenamiento)
     * `exercise_needs` (Necesidades de ejercicio)
     * `good_with_kids` (Comportamiento con niños)
   - Coloreado por categoría de tamaño
   - Diagonal: histogramas de cada feature
   - Fuera de diagonal: scatter plots de relaciones

3. **Distribución de Características**
   - 9 histogramas mostrando frecuencia de valores 1-5
   - Una visualización por cada característica del dataset
   - Identifica patrones y tendencias generales

4. **Mapa de Correlación (Heatmap)**
   - Matriz de correlaciones entre todas las características
   - Valores de -1 a 1 mostrando relaciones positivas/negativas
   - Útil para feature engineering y selección de variables

5. **Scatter Plot: Energía vs Entrenabilidad**
   - Visualiza relación entre nivel de energía y facilidad de entrenamiento
   - Tamaño de puntos representa tamaño de raza
   - Colores indican nivel de energía
   - Identifica clusters naturales de razas

6. **Top 10 Razas - Mayor Energía**
   - Ranking de razas más activas
   - Ideal para personas deportistas o con estilo de vida activo

7. **Top 10 Razas - Más Entrenables**
   - Ranking de razas más fáciles de entrenar
   - Recomendado para dueños primerizos

#### 🔍 Conclusiones del Análisis
- Distribución equilibrada de características
- Correlaciones identificadas entre features
- Variedad de tamaños representada
- Patrones de comportamiento por tipo de raza

**Utilidad**:
- Transparencia sobre los datos usados en el modelo
- Validación de calidad del dataset
- Identificación de sesgos o gaps
- Justificación de decisiones de ML

---

## Ejemplos de Uso

### Ejemplo 1: Familia con Niños Pequeños

**Escenario**: Familia con niños de 3-8 años, casa con jardín, primera vez con perro

**Preferencias**:
```
size: 3                      (Tamaño mediano)
good_with_children: 5        (Excelente con niños)
good_with_other_dogs: 4      (Muy sociable)
shedding_level: 2            (Poca muda)
grooming_level: 2            (Bajo mantenimiento)
trainability: 5              (Muy fácil de entrenar)
barking_level: 2             (Poco ruidoso)
energy_level: 3              (Energía moderada)
protectiveness: 3            (Protector moderado)
playfulness: 5               (Muy juguetón)
```

**Razas Recomendadas Esperadas**:
- Golden Retriever (95% compatibilidad)
- Labrador Retriever (94% compatibilidad)
- Beagle (88% compatibilidad)
- Cavalier King Charles Spaniel (87% compatibilidad)
- Cocker Spaniel (85% compatibilidad)

---

### Ejemplo 2: Persona en Apartamento

**Escenario**: Soltero en apartamento pequeño, trabaja desde casa, primera vez con mascota

**Preferencias**:
```
size: 1                      (Muy pequeño)
good_with_children: 3        (Indiferente)
good_with_other_dogs: 4      (Sociable)
shedding_level: 1            (Muy poca muda)
grooming_level: 3            (Mantenimiento moderado)
trainability: 4              (Fácil de entrenar)
barking_level: 1             (Muy silencioso)
energy_level: 2              (Baja energía)
protectiveness: 2            (Poco protector)
playfulness: 3               (Moderadamente juguetón)
```

**Razas Recomendadas Esperadas**:
- French Bulldog (92% compatibilidad)
- Pug (90% compatibilidad)
- Shih Tzu (88% compatibilidad)
- Bichon Frise (86% compatibilidad)
- Boston Terrier (84% compatibilidad)

---

### Ejemplo 3: Deportista Activo

**Escenario**: Persona activa, corre diariamente, busca compañero de ejercicio

**Preferencias**:
```
size: 4                      (Grande)
good_with_children: 3        (Indiferente)
good_with_other_dogs: 5      (Muy sociable)
shedding_level: 3            (Muda moderada aceptable)
grooming_level: 2            (Bajo mantenimiento)
trainability: 5              (Muy entrenable)
barking_level: 2             (Poco ruidoso)
energy_level: 5              (Muy alta energía)
protectiveness: 4            (Buen guardián)
playfulness: 5               (Muy juguetón)
```

**Razas Recomendadas Esperadas**:
- Border Collie (96% compatibilidad)
- Australian Shepherd (94% compatibilidad)
- Labrador Retriever (92% compatibilidad)
- Vizsla (91% compatibilidad)
- German Shorthaired Pointer (89% compatibilidad)

---

## Pruebas con Diferentes Herramientas

### Usando curl (Terminal)

#### Test 1: Obtener Home Page
```bash
curl http://localhost:8000/
```

#### Test 2: Ver Catálogo de Razas
```bash
curl http://localhost:8000/breeds
```

#### Test 3: Solicitar Recomendación
```bash
curl -X POST "http://localhost:8000/recommend" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "size=3&good_with_children=5&good_with_other_dogs=4&shedding_level=2&grooming_level=2&trainability=4&barking_level=2&energy_level=3&protectiveness=4&playfulness=4"
```

---

### Usando Postman

#### Paso 1: Crear Nueva Request

1. Abrir Postman
2. Clic en "New" → "HTTP Request"
3. Configurar:
   - **Método**: POST
   - **URL**: `http://localhost:8000/recommend`

#### Paso 2: Configurar Body

1. Seleccionar tab "Body"
2. Elegir "x-www-form-urlencoded"
3. Agregar key-value pairs:

| Key | Value |
|-----|-------|
| size | 3 |
| good_with_children | 5 |
| good_with_other_dogs | 4 |
| shedding_level | 2 |
| grooming_level | 2 |
| trainability | 4 |
| barking_level | 2 |
| energy_level | 3 |
| protectiveness | 4 |
| playfulness | 4 |

#### Paso 3: Enviar Request

Clic en "Send" → Recibir respuesta HTML con recomendaciones

---

### Usando Swagger UI (Recomendado)

#### Paso 1: Acceder a Swagger
```
http://localhost:8000/docs
```

#### Paso 2: Probar Endpoint POST /recommend

1. Expandir sección "POST /recommend"
2. Clic en "Try it out"
3. Completar formulario con valores de ejemplo
4. Clic en "Execute"
5. Ver respuesta en "Response body"

**Ventajas de Swagger UI**:
- Interfaz visual intuitiva
- Validación automática de parámetros
- Generación de código ejemplo
- Testing en vivo

#### Paso 3: Ver Esquemas

Swagger UI muestra automáticamente:
- Tipos de datos esperados
- Validaciones (min/max valores)
- Campos requeridos vs opcionales
- Ejemplos de respuesta

---

### Usando Python Requests

```python
import requests

# URL del servidor
base_url = "http://localhost:8000"

# Preferencias del usuario
preferences = {
    "size": 3,
    "good_with_children": 5,
    "good_with_other_dogs": 4,
    "shedding_level": 2,
    "grooming_level": 2,
    "trainability": 4,
    "barking_level": 2,
    "energy_level": 3,
    "protectiveness": 4,
    "playfulness": 4
}

# Enviar solicitud
response = requests.post(
    f"{base_url}/recommend",
    data=preferences
)

# Verificar respuesta
if response.status_code == 200:
    print("✓ Recomendación exitosa")
    print(response.text[:500])  # Primeros 500 caracteres HTML
else:
    print(f"✗ Error: {response.status_code}")
```

---

### Usando JavaScript (Fetch API)

```javascript
// Preferencias del usuario
const preferences = {
    size: 3,
    good_with_children: 5,
    good_with_other_dogs: 4,
    shedding_level: 2,
    grooming_level: 2,
    trainability: 4,
    barking_level: 2,
    energy_level: 3,
    protectiveness: 4,
    playfulness: 4
};

// Convertir a URLSearchParams
const formData = new URLSearchParams(preferences);

// Enviar solicitud
fetch('http://localhost:8000/recommend', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: formData
})
.then(response => response.text())
.then(html => {
    console.log('✓ Recomendación recibida');
    // Insertar HTML en página
    document.getElementById('results').innerHTML = html;
})
.catch(error => {
    console.error('✗ Error:', error);
});
```

---

## Interpretación de Resultados

### Estructura de la Respuesta

Al hacer una solicitud POST a `/recommend`, recibes una página HTML con:

#### 1. Header con Información
```
Tus Razas Recomendadas
Basado en tus preferencias, estas son las mejores opciones:
```

#### 2. Top 5 Razas Recomendadas

Cada raza incluye:

**Nombre de la Raza**
- Ejemplo: "Golden Retriever"

**Porcentaje de Compatibilidad**
- Rango: 0-100%
- Cálculo: Basado en similitud euclidiana inversa
- Interpretación:
  - 90-100%: Excelente match
  - 80-89%: Muy buena compatibilidad
  - 70-79%: Buena opción
  - 60-69%: Opción viable con ajustes
  - <60%: No recomendado

**Características de la Raza** (10 barras de progreso):

| Característica | Valores | Interpretación |
|----------------|---------|----------------|
| **Tamaño** | 1-5 | 1=Toy, 2=Pequeño, 3=Mediano, 4=Grande, 5=Gigante |
| **Bueno con Niños** | 1-5 | Nivel de paciencia y gentileza con niños |
| **Bueno con Perros** | 1-5 | Sociabilidad con otros caninos |
| **Nivel de Muda** | 1-5 | Cantidad de pelo que suelta |
| **Necesidad Aseo** | 1-5 | Frecuencia de grooming requerida |
| **Entrenabilidad** | 1-5 | Facilidad para aprender comandos |
| **Nivel Ladridos** | 1-5 | Tendencia a vocalizar |
| **Energía** | 1-5 | Necesidad de actividad física |
| **Protección** | 1-5 | Instinto de guardián |
| **Juguetón** | 1-5 | Amor por el juego y actividades |

#### 3. Imagen de la Raza
- Foto representativa de la raza
- Tamaño: 180px circular
- Fuente: API de placedog.net

#### 4. Botón de Acción
```
"Buscar otra raza" → Regresa al formulario
```

---

### Ejemplo de Resultado Completo

```
RESULTADO PARA FAMILIA CON NIÑOS

TOP 5 RAZAS RECOMENDADAS:

1. Golden Retriever - 95% Compatible ⭐⭐⭐⭐⭐
   • Tamaño: ████░ (4/5) - Grande
   • Bueno con Niños: █████ (5/5) - Excelente
   • Energía: ████░ (4/5) - Alta
   • Entrenabilidad: █████ (5/5) - Muy fácil
   [Imagen del Golden Retriever]

2. Labrador Retriever - 94% Compatible ⭐⭐⭐⭐⭐
   • Tamaño: ████░ (4/5) - Grande
   • Bueno con Niños: █████ (5/5) - Excelente
   • Energía: █████ (5/5) - Muy alta
   • Entrenabilidad: █████ (5/5) - Muy fácil
   [Imagen del Labrador]

3. Beagle - 88% Compatible ⭐⭐⭐⭐
   • Tamaño: ███░░ (3/5) - Mediano
   • Bueno con Niños: █████ (5/5) - Excelente
   • Energía: ████░ (4/5) - Alta
   • Entrenabilidad: ███░░ (3/5) - Moderada
   [Imagen del Beagle]

... (2 razas más)
```

---

### Factores que Influyen en el Porcentaje

El algoritmo considera:

1. **Distancia Euclidiana**: Similitud matemática entre tus preferencias y cada raza
2. **Ponderación de Features**: Algunas características tienen mayor peso
3. **Normalización**: Todas las características se escalan de 0 a 1
4. **Clustering**: Agrupa razas similares para diversidad en resultados

**Fórmula Simplificada**:
```
Compatibilidad (%) = 100 - (distancia_euclidiana × 20)

Donde distancia_euclidiana se calcula como:
√Σ(preferencia_usuario - caracteristica_raza)²
```

---

### Recomendaciones de Uso

#### Para Mejores Resultados:

1. **Sé honesto con tus preferencias**
   - No ingreses valores ideales, sino lo que realmente necesitas

2. **Considera tu estilo de vida real**
   - Tiempo disponible para ejercicio
   - Espacio en tu hogar
   - Experiencia previa con perros

3. **Prioriza características importantes**
   - Si tienes niños pequeños → `good_with_children = 5`
   - Si vives en apartamento → `size = 1 o 2`, `barking_level = 1`
   - Si eres activo → `energy_level = 4 o 5`

4. **Explora el catálogo completo**
   - Usa `/breeds` para ver todas las opciones
   - Compara características entre razas
   - Lee descripciones detalladas

5. **Prueba diferentes combinaciones**
   - Ajusta 1-2 parámetros a la vez
   - Observa cómo cambian las recomendaciones
   - Encuentra el balance perfecto

---

### Códigos de Estado HTTP

| Código | Significado | Acción |
|--------|-------------|--------|
| 200 | **Éxito | Recomendación generada correctamente |
| 400 | ⚠️ Bad Request | Verificar parámetros del formulario |
| 404 | ❌ Not Found | Endpoint incorrecto |
| 422 | ⚠️ Validation Error | Valores fuera de rango (1-5) |
| 500 | ❌ Server Error | Error interno (contactar soporte) |

---

### Preguntas Frecuentes (FAQ)

**Q: ¿Cuántas razas puedo recibir en la recomendación?**
A: El sistema retorna las Top 5 razas más compatibles.

**Q: ¿Puedo solicitar más o menos razas?**
A: Actualmente está fijado en 5, pero puedes modificar `top_n` en el código.

**Q: ¿Los resultados cambian cada vez?**
A: No, son determinísticos. Mismas preferencias = mismos resultados.

**Q: ¿Qué pasa si todas las razas tienen baja compatibilidad?**
A: El sistema siempre retorna las 5 mejores, incluso si el porcentaje es bajo (<60%).

**Q: ¿Puedo obtener la respuesta en JSON?**
A: Actualmente solo HTML. Para JSON, modifica el endpoint en `dog_controller.py`.

**Q: ¿Las imágenes son reales?**
A: Sí, provienen de APIs públicas de imágenes de perros.

---

## Próximos Pasos

Ahora que conoces la API:

1. Lee la [Documentación Técnica](03_DOCUMENTACION_TECNICA.md) para entender el funcionamiento interno
2. Consulta el [Manual de Datos](04_MANUAL_DATOS.md) para conocer el dataset en profundidad
3. ¡Empieza a encontrar la raza perfecta!

---

**¿Necesitas ayuda?** Visita `/docs` para documentación interactiva o consulta los otros manuales.
