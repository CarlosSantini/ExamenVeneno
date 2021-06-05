import pandas as pd
from src import config

def feature_process(veneno, sustancias_diversas):

    '''Limpieza de datos'''
    # - Explorar archivos csv
    # print(veneno.head())
    # print(veneno.columns)

    # print(sustancias_diversas.head())
    # print(sustancias_diversas.columns)

    # - Tipo de los datos
    # veneno.info()
    # sustancias_diversas.info()

    # - Revisar si hay valores nulos, y si hay datos nulos, contar cuantos
    null_sustancias = sustancias_diversas.isnull().values.any()
    # print(null_sustancias)

    sustancias_diversas.isnull().sum()

    # - Eliminar la columna "caracteristica" de veneno
    veneno = veneno.drop(labels='caracteristica', axis=1)
    # print(veneno)

    # - Buscar filas duplicadas
    duplicados = sustancias_diversas[sustancias_diversas.duplicated()]
    # print(duplicados)

    # - Buscar ID de rios repetidos
    id_duplicados = sustancias_diversas[sustancias_diversas.duplicated('id')]
    # print(id_duplicados)

    return veneno, sustancias_diversas

