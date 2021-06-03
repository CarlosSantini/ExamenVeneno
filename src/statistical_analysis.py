


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
