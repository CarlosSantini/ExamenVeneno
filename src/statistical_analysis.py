import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def plot_boxplot(vals, veneno):
    sns.set(style="darkgrid")

    for _, val in enumerate(vals.columns):
        fig, (ax_hist, ax_box) = plt.subplots(1, 2)
        sns.histplot(data=vals[val], ax=ax_hist)
        sns.boxplot(data=vals[val], ax=ax_box, color='green')

        ax_hist.set_xlabel(xlabel='Cantidad de veneno', fontsize=15)
        ax_hist.set_ylabel(ylabel='Instancias', fontsize=15)

        ax_box.set_xlabel(xlabel=val, fontsize=15)
        ax_box.set_ylabel(ylabel='Cantidad de veneno', fontsize=15)

        fig.set_size_inches(12, 6)
        fig.subplots_adjust(wspace=.25, left=0.035, right=.985, top=.925, bottom=.1)
        fig.suptitle(val + " con cantidad minima de sustancia venenosa: " + str(veneno[val][0]), fontsize=20)
        plt.savefig("../plots/HistnBox " + val + ".png")
        plt.show()



def agregar_texto_bar(totales):
    i = 0
    for key in totales:
        #  print(key ,":", totales[key])
        plt.text(x=i, y=totales[key]+1, s=str(totales[key]), fontdict=dict(fontsize=15))
        i += 1


def plot_total_instances(totales):
    plt.figure(figsize=(22, 8))
    plt.bar(*zip(*totales.items()))

    plt.title(label='Total de instancias mayor igual al minimo de cada caracteristica', fontsize=20)
    plt.xlabel(xlabel='Veneno', fontsize=16)
    plt.ylabel(ylabel='Instancias', fontsize=16)

    agregar_texto_bar(totales)
    plt.savefig("../plots/Total de Instancias.png")
    plt.show()



def compute_descriptive_stats(instancias):
    # - Calcular media, mediana, moda, maximo, minimo de cada caracteristica de veneno a partir del total de
    # instancias que cumplen el valor minimo de veneno
    total = instancias.count()
    media = instancias.mean()
    mediana = instancias.median()
    modaa = instancias.mode().max()  # Regresa la moda del numero mas grande
    maax = instancias.max()
    miin = instancias.min()
    desv = instancias.std()
    description = pd.DataFrame(np.array([total, media, mediana, desv, modaa, maax, miin]),
                               index=["Total", "Media", "Mediana", "Std", "Moda", "Maximo", "Minimo"],
                               columns=[instancias.keys()])
    print(description)

    # instancias.describe()

    return description


def tabla_cumplimineto_requisito(ids):
    vals = pd.concat(
        [ids[0]['v1'], ids[1]['v2'], ids[2]['v3'], ids[3]['v4'], ids[4]['v5'], ids[5]['v6'], ids[6]['v7'], ids[7]['v8'],
         ids[8]['v9'], ids[9]['v10']], ignore_index=True, axis=1)

    vals = vals.rename(columns={0: 'v1', 1: 'v2', 2: 'v3', 3: 'v4', 4: 'v5', 5: 'v6', 6: 'v7', 7: 'v8', 8: 'v9', 9: 'v10'})
    return vals


def exploration_data(veneno, sustancias_diversas):
    # - ¿Cuales son las instancias que son mayor o igual a la caracteristica minima requerida y a su vez
    #   contar cuantos hacen match en el dataset para cada caracterisca?
    ids = list()
    totales = dict()

    for idx, val in enumerate(veneno):
        #     print(val)
        a = sustancias_diversas[sustancias_diversas[val] >= veneno[val].item()]
        ids.append(a)
        totales[val] = a[val].count()

    print(ids)
    print()
    print(totales)

    # - Obtener y Ordenar el total de instancias para cada caracteristica del veneno
    tuplas_ordered = reversed(sorted(totales.items(), key=lambda x:x[1]))
    totales_ordered = {key : val for key, val in tuplas_ordered}
    print(totales_ordered)

    # - Crear una tabla con las instancias que si cumplen el requesito para cada caracteristica del veneno, las que
    # no lo cumplen, rellenar con valor nulo.
    instancias = tabla_cumplimineto_requisito(ids)

    # - Grafica que muestra cuantas instancias son mayor igual al minimo de cada caracteristica
    plot_total_instances(totales)

    # - Calcular analisis estadistico descriptivo
    description = compute_descriptive_stats(instancias)

    # - Boxplot de Distribución de las instancias del veneno entre cada caracteristica
    plot_boxplot(instancias, veneno)

    # - Buscar correlacion entre






