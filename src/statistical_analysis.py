import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.conditions import first_condition, second_condition, third_condition, fourth_condition, fifth_condition, sixth_condition
import os


def plot_boxplot(vals, veneno):
    sns.set(style="darkgrid")
    ruta = os.path.join(os.path.abspath(os.getcwd()), 'plots')

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
        plt.savefig(ruta+"\HistnBox " + val + ".png")
        # plt.show()


def plot_all_boxplots(vals):
    plt.figure(figsize=(22, 8))
    ax = sns.boxenplot(data=vals, palette="Set2", showfliers=False)
    ax = sns.stripplot(data=vals, size=4, color=".26")
    ax.set_title(label='Distribucion de las instancias del veneno entre cada caracteristica ', fontsize=20)
    ax.set_xlabel(xlabel='Caracteristica del Veneno', fontsize=16)
    ax.set_ylabel(ylabel='Cantidad de sustancia\n de veneno', fontsize=16)
    plt.grid()
    ruta = os.path.join(os.path.abspath(os.getcwd()), 'plots')
    plt.savefig(ruta+"\All Boxplots.png")
    # plt.show()


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
    ruta = os.path.join(os.path.abspath(os.getcwd()), 'plots')
    plt.savefig(ruta+"\Total de Instancias.png")
    # plt.show()


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
    # print(description)

    # instancias.describe()
    return description


def find_correlation(instancias, metodo):
    correlations = round(instancias.corr(method=metodo), 5)
    # print(correlations)
    return correlations


def tabla_cumplimineto_requisito(ids):
    vals = pd.concat(
        [ids[0]['v1'], ids[1]['v2'], ids[2]['v3'], ids[3]['v4'], ids[4]['v5'], ids[5]['v6'], ids[6]['v7'], ids[7]['v8'],
         ids[8]['v9'], ids[9]['v10']], ignore_index=True, axis=1)

    vals = vals.rename(columns={0: 'v1', 1: 'v2', 2: 'v3', 3: 'v4', 4: 'v5', 5: 'v6', 6: 'v7', 7: 'v8', 8: 'v9', 9: 'v10'})
    return vals


def exploration_data(veneno, sustancias_diversas):
    # - ??Cuales son las instancias que son mayor o igual a la caracteristica minima requerida y a su vez
    #   contar cuantos hacen match en el dataset para cada caracterisca?
    ids = list()
    totales = dict()

    for idx, val in enumerate(veneno):
        #     print(val)
        a = sustancias_diversas[sustancias_diversas[val] >= veneno[val].item()]
        ids.append(a)
        totales[val] = a[val].count()

    # print(ids)
    # print()
    # print(totales)

    # - Obtener y Ordenar el total de instancias para cada caracteristica del veneno
    tuplas_ordered = reversed(sorted(totales.items(), key=lambda x:x[1]))
    totales_ordered = {key : val for key, val in tuplas_ordered}
    # print(totales_ordered)

    # - Crear una tabla con las instancias que si cumplen el requesito para cada caracteristica del veneno, las que
    # no lo cumplen, rellenar con valor nulo.
    instancias = tabla_cumplimineto_requisito(ids)

    # - Grafica que muestra cuantas instancias son mayor igual al minimo de cada caracteristica
    plot_total_instances(totales)

    # - Calcular analisis estadistico descriptivo
    description = compute_descriptive_stats(instancias)

    # - Boxplot general de la distribuci??n de las instancias del veneno entre cada caracteristica
    plot_all_boxplots(instancias)

    # - Boxplot de Distribuci??n de las instancias del veneno entre cada caracteristica
    plot_boxplot(instancias, veneno)

    # - Buscar correlacion entre
    correl = find_correlation(instancias, 'pearson')

    # - Guardar muestras que cumplan las condicisiones
    rios_cincuenta = pd.DataFrame(columns=instancias.columns)

    all_samples, final_samples = first_condition(sustancias_diversas, veneno)
    nine_max_chars, final_samples = second_condition(final_samples, veneno)
    six_charac_eq_m, final_samples = third_condition(final_samples)
    six_charac_eq_m1, final_samples = fourth_condition(final_samples)
    six_charac_gt_m, final_samples = fifth_condition(final_samples)
    six_charac_gt_m1 = sixth_condition(final_samples)

    rios_cincuenta = pd.concat([all_samples,
                                nine_max_chars,
                                six_charac_eq_m,
                                six_charac_eq_m1,
                                six_charac_gt_m,
                                six_charac_gt_m1
                                ], ignore_index=True)

    # - Eliminar del dataframe las muestras que sobrepasen el tama??o de la tabla igual a 50
    rios_cincuenta = rios_cincuenta.drop(rios_cincuenta.index[-(len(rios_cincuenta)-50):])

    # print(rios_cincuenta)

    ruta = os.path.join(os.path.abspath(os.getcwd()),'data')
    rios_cincuenta.to_csv(ruta+"\\urgente_orden_de_cierre.csv", index=False)






