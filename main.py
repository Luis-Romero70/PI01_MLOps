from fastapi import FastAPI
import pandas as pd
from fuzzywuzzy import fuzz

df_movies = pd.read_csv('movies_ETL.csv')

app = FastAPI()

@app.get('/peliculas-idioma/{idioma}')
def peliculas_idioma(Idioma: str):
    # Filtrar las películas por idioma
    peliculas_filtradas = df_movies[df_movies['original_language'] == Idioma]
    
    # Obtener la cantidad de películas filtradas
    cantidad_peliculas = len(peliculas_filtradas)
    
    # Generar el mensaje de retorno
    mensaje_retorno = f"Hay {cantidad_peliculas} película(s) que fueron estrenadas en {Idioma}"
    
    return mensaje_retorno
    
@app.get('/peliculas-duracion/{pelicula}')
def peliculas_duracion(Pelicula: str):
    # Filtrar las películas por nombre
    pelicula_filtrada = df_movies[df_movies['title'] == Pelicula]
    
    # Verificar si se encontró la película
    if len(pelicula_filtrada) == 0:
        return "No se encontró la película especificada. Verifique el nombre e ingréselo nuevamente"
    
    # Obtener la duración y el año de estreno de la película
    duracion = pelicula_filtrada['runtime'].values[0]
    anio_estreno = pelicula_filtrada['release_year'].values[0]
    
    # Generar el mensaje de retorno
    mensaje_retorno = f"{Pelicula}. Duración: {duracion}. Año de estreno: {anio_estreno}"
    
    return mensaje_retorno

@app.get('/franquicia/{franquicia}')
def franquicia(Franquicia: str):
    # Filtrar las películas por pertenecer a la franquicia especificada
    peliculas_franquicia = df_movies[df_movies['franquicia'] == Franquicia]
    
    # Verificar si se encontraron películas para la franquicia especificada
    if len(peliculas_franquicia) == 0:
        return "No se encontraron películas para la franquicia especificada."
    
    # Obtener la cantidad de películas, ganancia total y ganancia promedio
    cantidad_peliculas = len(peliculas_franquicia)
    ganancia_total = (peliculas_franquicia['revenue'] - peliculas_franquicia['budget']).sum()
    ganancia_promedio = (peliculas_franquicia['revenue'] - peliculas_franquicia['budget']).mean()
    
    # Generar el mensaje de retorno
    mensaje_retorno = f"La franquicia {Franquicia} posee {cantidad_peliculas} películas, una ganancia total de {ganancia_total}, y una ganancia promedio de {ganancia_promedio}."
    
    return mensaje_retorno

@app.get('/peliculas-pais/{pais}')
def peliculas_pais(Pais: str):
    # Filtrar las películas por país de producción
    peliculas_pais = df_movies[df_movies['países'].apply(lambda paises: Pais in paises)]
    
    # Obtener la cantidad de películas producidas en el país
    cantidad_peliculas = len(peliculas_pais)
    
    # Generar el mensaje de retorno
    mensaje_retorno = f"Se produjeron {cantidad_peliculas} películas en el país {Pais}."
    
    return mensaje_retorno

@app.get('/productoras-exitosas/{productora}')
def productoras_exitosas(Productora: str):
    # Filtrar las películas por productora
    películas_productora = df_movies[df_movies['productoras'].apply(lambda compañías: Productora in compañías)]
    
    # Calcular la recaudación total
    recaudación_total = películas_productora['revenue'].sum()
    
    # Obtener la cantidad de películas producidas
    cantidad_peliculas = len(películas_productora)
    
    # Generar el mensaje de retorno
    mensaje_retorno = f"La productora {Productora} ha tenido una recaudación total de {recaudación_total}, con un total de {cantidad_peliculas} películas producidas."
    
    return mensaje_retorno

@app.get('/get-director/{nombre_director}')
def get_director(nombre_director):
    # Filtrar las películas por director
    películas_director = df_movies[df_movies['director'].notnull() & (df_movies['director'] == nombre_director)]
    
    # Calcular el retorno total del director
    retorno_total = películas_director['revenue'].sum()
    
    # Generar una lista de información detallada de cada película
    películas_info = []
    for index, row in películas_director.iterrows():
        película = {
            'nombre': row['title'],
            'fecha_lanzamiento': row['release_date'],
            'retorno': row['revenue'],
            'costo': row['budget'],
            'ganancia': row['revenue'] - row['budget']
        }
        películas_info.append(película)
    
    # Generar el mensaje de retorno
    mensaje_retorno = f"El director {nombre_director} ha logrado un retorno de {retorno_total}."
    
    return mensaje_retorno, películas_info

# Función para obtener los 3 primeros actores
def get_top_actors(elenco):
    if isinstance(elenco, list):
        actors = elenco[:3]
        return actors
    else:
        return []

@app.get('/recomendacion/{titulo}')
def recomendacion(titulo):
    # Preprocesamiento de datos
    df_movies_expanded = df_movies.explode('géneros')
    df_movies_expanded['géneros'] = df_movies_expanded['géneros'].astype(str)
    df_movies_expanded['popularity'] = df_movies_expanded['popularity'].astype(float)

    # Filtrar la película de referencia
    df_ref_movie = df_movies_expanded[df_movies_expanded['title'] == titulo]
    ref_genres = set(df_ref_movie['géneros'])
    ref_franchise = df_ref_movie['franquicia'].iloc[0]
    ref_actors = set(df_ref_movie['elenco'].apply(get_top_actors).iloc[0])

    # Calcular la puntuación de similitud
    df_movies_filtered = df_movies_expanded[df_movies_expanded['title'] != titulo]
    df_movies_filtered['similarity_score'] = (df_movies_filtered['géneros'].apply(lambda genres: len(set(genres) & ref_genres)) * 15 +
                                               (df_movies_filtered['franquicia'] == ref_franchise).astype(int) * 10 +
                                               (df_movies_filtered['popularity'] * 0.0001) +
                                               df_movies_filtered['title'].apply(lambda x: fuzz.ratio(x, titulo)) * 0.01 +
                                               df_movies_filtered['elenco'].apply(lambda elenco: len(set(get_top_actors(elenco)) & ref_actors)) * 1)

    # Ordenar las películas según la puntuación de similitud
    df_movies_sorted = df_movies_filtered.sort_values('similarity_score', ascending=False)

    # Generar las recomendaciones
    top_recommendations = df_movies_sorted['title'].head(5).tolist()

    return top_recommendations





if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
