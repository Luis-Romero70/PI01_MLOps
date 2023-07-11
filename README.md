<h1 align='center' style="font-weight:light; text-align:justify; margin-left: 80px; margin-right: 100px;">
Proyecto de Data Science para un Sistema de Recomendación de Películas
</h1>

<h1 align='center'>
<img src="Pop_corn.png" width="30"> 
PI01_MLOps
<img src="Ticket.png" width="30">


</h1>


# Introducción:
En este laboratorio individual de _Machine Learning Operations_ (MLOps), se llevará a cabo el desarrollo de un modelo de clasificación para un sistema de recomendación de películas. El objetivo principal es, asumiendo el rol de un MLOps Engineer, poder aplicar las prácticas y conceptos de MLOps en todas las etapas del proyecto, desde la preparación y transformación de los datos hasta el despliegue del modelo y la generación de API para consultas de recomendaciones.

# Objetivos del proyecto:
**1. Preparación y transformación de datos:** Realizar el proceso de extracción, transformación y carga (ETL) de los datos de películas para su posterior análisis y entrenamiento del modelo.<br>
**2. Análisis exploratorio de datos (EDA):** Realizar un análisis exhaustivo de los datos de películas, explorando las características y relaciones entre variables, identificando patrones y preparando los datos para el modelo de clasificación.<br>
**3. Implementación de API para consultas específicas:** Generar una interfaz de consulta donde los usuarios puedan ingresar criterios de búsqueda y obtener respuestas a sus consutas.<br>
**4. Desarrollo del modelo de clasificación:** Implementar un modelo de clasificación utilizando técnicas de Machine Learning, que permita recomendar películas en base a características específicas.<br>
**5. Despliegue del modelo y la API:** Desplegar el modelo y la API en una plataforma o entorno de producción para que esté disponible y accesible para los usuarios finales.

# Resumen de los procesos:
**1. Extracción, Transformación y Carga (ETL):** Se realizará el proceso de extracción de datos de películas, su transformación para limpieza y preparación, y finalmente su carga en un formato adecuado para su posterior análisis y entrenamiento del modelo.<br>
**2. Análisis Exploratorio de Datos (EDA):** Se realizará un análisis detallado de los datos de películas, explorando características clave, identificando patrones y relaciones entre variables, y tomando decisiones sobre el tratamiento de datos faltantes o inconsistentes.<br>
**3. Implementación de API para consultas específicas:** Se generarán funciones de consulta, siguiendo las pautas presentadas para este laboratorio, y se creará una interfaz de consulta donde los usuarios puedan ingresar sus preferencias y obtener recomendaciones de películas acorde a los criterios seleccionados. Esto último se realizará utilizando FastAPI.<br>
**4. Desarrollo del Modelo de Recomendación:** Se implementará un modelo de recomendación utilizando técnicas de Machine Learning para generar sugerencias de películas basadas en las preferencias de los usuarios. A partir de título que ingresará el usuario, el modelo tomará un grupo de parámetros para evaluar el grado de semejanza con otras películas del data set, y devolverá una lista con los títulos de las 5 (cinco) películas que posean los mayores grados de similitud, de acuerdo a los parámetros seleccionados.<br>
**5. Despliegue del modelo y la API:** Se llevará a cabo el despliegue del modelo y la API en un entorno de producción, asegurando la disponibilidad y accesibilidad para los usuarios finales. Este proceso se llevará a cabo mediante el uso de Render.

# Herramientas Utilizadas:
- Scikit Learn: Utilizado para el modelo de clasificación.
- Python: Lenguaje de programación principal utilizado en el desarrollo del proyecto.
- Pandas: Utilizado para la manipulación y análisis de datos estructurados.
- NumPy: Utilizado para realizar operaciones numéricas y manipulación de datos.
- FastAPI: Utilizado para la implementación de la API de consultas de recomendaciones.
- Render: Plataforma utilizada para el despliegue en la nube del modelo y la API.

# Etapas del Proyecto:
## 1. Preparación y Transformación de Datos:
   - Extracción de datos de películas de fuentes relevantes.
   - Limpieza y preprocesamiento de datos para eliminar valores atípicos y datos faltantes.
   - Transformación de variables categóricas y codificación de características relevantes.
   - Generación de un dataset limpio y listo para su análisis y entrenamiento del modelo.
   - Link para el notebook donde se implementó el ETL: (https://github.com/Luis-Romero70/PI01_MLOps/blob/master/Lab01_MLOps_ETL.ipynb)

## 2. Análisis Exploratorio de Datos (EDA):
   - Exploración visual y estadística de las variables de interés.
   - Identificación de patrones, correlaciones y relaciones entre variables.
   - Selección de características relevantes para el modelo de clasificación.
   - Tratamiento de datos faltantes, inconsistentes o ruidosos.
   - Visualización de los resultados del análisis exploratorio a través de gráficos y tablas informativas.
   - Link para el notebook donde se implementó el EDA: (https://github.com/Luis-Romero70/PI01_MLOps/blob/master/Lab01_EDA.ipynb)

## 3. Implementación de API para Consultas de Recomendaciones:
   - Generación de las funciones de consulta específica, según los requerimientos presentados para este laboratorio.
   - Creación de una interfaz de consulta interactiva donde los usuarios puedan ingresar sus preferencias de películas.
   - Procesamiento de las consultas.
   - Presentación de las respuestas a los usuarios de forma clara y comprensible.
   - Link para el notebook donde se implementaron las funciones de consulta para la API: (https://github.com/Luis-Romero70/PI01_MLOps/blob/master/Lab01_Funciones_API.ipynb)

## 4. Desarrollo del Modelo de Recomendación:
   - Selección del algoritmo de recomendación más adecuado para el caso de recomendación de películas.
   - Elección de los parámetros (`campos`) que se emplearán para la caracterización de las películas del dataset.
   - Entrenamiento y ajuste del modelo utilizando el dataset preparado en las etapas anteriores.
   - Optimización del modelo para mejorar su precisión y capacidad de recomendación (ajuste de coeficientes).
   - Link para el notebook donde se desarrolló el modelo de clasificación y recomendació: (https://github.com/Luis-Romero70/PI01_MLOps/blob/master/Lab01_ML_Recomendación.ipynb)

## 5. Deployment de la API:
   
   - Deployment de la API empleando Render.
   - Link del archivo `.py` que contiene el código de la API generada, incluyendo las 6 (seis) consultas y el sistema de recomendación: (https://github.com/Luis-Romero70/PI01_MLOps/blob/master/main.py)
   - URL de la API desplegada: (https://proyectodsft12-01-mlops.onrender.com/docs)

# Conclusiones:
En este laboratorio individual de ML Ops, se ha llevado a cabo el desarrollo de un modelo de clasificación para un sistema de recomendación de películas. Se han aplicado prácticas y conceptos de ML Ops en todas las etapas del proyecto, desde la preparación y transformación de los datos hasta el despliegue del modelo y la generación de API para consultas de recomendaciones. El proyecto ha permitido familiarizarse con herramientas y técnicas fundamentales en el ámbito de ML Ops, como el análisis exploratorio de datos, la implementación de modelos de clasificación y la creación de API para consultas. Además, se ha puesto énfasis en la calidad, reproducibilidad y mantenibilidad del proyecto, siguiendo las mejores prácticas en ciencia de datos y ML Ops.

## Links

- API de consulta de películas y modelo de sistema de recomendación[https://proyectodsft12-01-mlops.onrender.com/docs#/]
- Videotutorial del trabajo realizado en YouTube:[https://youtu.be/eq5kRkk2V7s]

## Recomendaciones

- Para la función `peliculas_idioma`, ingresar solamente las abreviaturas del idioma (por ejemplo, "inglés" sería "en", "español" sería "es").

**Autor:** <br>
Luis Eduardo Romero

Correo electrónico: romero.luis.eduardo70@gmail.com

LinkedIn: www.linkedin.com/in/luis-romero-97a7132b
