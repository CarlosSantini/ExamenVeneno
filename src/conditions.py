import pandas as pd


def first_condition(sustancias_diversas, veneno):
    '''
    Esta funcion evalua que las muestras contengan todas
    las caracteristicas de veneno mayor o igual al minimo de veneno respectivamente
    '''

    final_samples = sustancias_diversas.copy(
        deep=True)  # dataframe que nos servira para ir quitando las muestras que cumplen con los requisitos
    all_samples = sustancias_diversas.copy(
        deep=True)  # dataframe para guardar los rios que tienen todas las caracteristcicas de sustancias venenosas

    all_samples = all_samples[(all_samples['v1'] >= veneno['v1'][0]) &
                              (all_samples['v2'] >= veneno['v2'][0]) &
                              (all_samples['v3'] >= veneno['v3'][0]) &
                              (all_samples['v4'] >= veneno['v4'][0]) &
                              (all_samples['v5'] >= veneno['v5'][0]) &
                              (all_samples['v6'] >= veneno['v6'][0]) &
                              (all_samples['v7'] >= veneno['v7'][0]) &
                              (all_samples['v8'] >= veneno['v8'][0]) &
                              (all_samples['v9'] >= veneno['v9'][0]) &
                              (all_samples['v10'] >= veneno['v10'][0])]
    # print(all_samples)

    # Match de las muestras que tienen todas las caracteristicas de sustancias nocivas contra todas las muestras
    duplicates = pd.merge(final_samples, all_samples, how='inner', left_index=True, right_index=True)
    # print(duplicates)

    # Eliminamos las muestras a utilizar del resto de muestras que no se analizaran
    final_samples = final_samples.drop(duplicates.index)

    return all_samples, final_samples


def second_condition(final_samples, veneno):
    '''
    Esta funcion evalua que las muestras contengan las 9
    las caracteristicas de veneno (con mas muestras) mayor o igual al minimo de veneno respectivamente
    '''
    nine_max_chars = final_samples[(final_samples['v1'] >= veneno['v1'][0]) &
                                   (final_samples['v2'] >= veneno['v2'][0]) &
                                   (final_samples['v3'] >= veneno['v3'][0]) &
                                   (final_samples['v4'] >= veneno['v4'][0]) &
                                   (final_samples['v5'] >= veneno['v5'][0]) &
                                   (final_samples['v6'] >= veneno['v6'][0]) &
                                   (final_samples['v7'] >= veneno['v7'][0]) &
                                   (final_samples['v8'] >= veneno['v8'][0]) &
                                   (final_samples['v10'] >= veneno['v10'][0])]

    # Solo regresa 2 instancias
    # nine_max_chars.count()
    # print(nine_max_chars)

    # # Match de las muestras que tienen todas las caracteristicas de sustancias nocivas contra todas las muestras
    duplicates = pd.merge(final_samples, nine_max_chars, how='inner', left_index=True, right_index=True)
    # print(duplicates)

    # # Eliminamos las muestras a utilizar del resto de muestras que no se analizaran
    final_samples = final_samples.drop(duplicates.index)

    return nine_max_chars, final_samples


def third_condition(final_samples):
    '''
    Esta funcion evalua que las muestras de las caracteristicas v2, v6, v7, v8, v10
    sean exactamente igual a la moda de cada caracteristica
    '''
    # Tomando exactamente la moda de esas caracteristicas
    six_charac_eq_m = final_samples[(final_samples['v2'] == 56.3) &
                                    (final_samples['v6'] == 1) &
                                    (final_samples['v7'] == 2.1) &
                                    (final_samples['v8'] == 3.8) &
                                    (final_samples['v10'] == 23.8)]  # &
    #                           (final_samples['v1'] == 21.1)]

    # obtenemos 5 muestras que cumplen el requisito
    # six_charac_eq_m.count()
    # print(six_charac_eq_m)

    # # # Match de las muestras que tienen todas las caracteristicas de sustancias nocivas contra todas las muestras
    duplicates = pd.merge(final_samples, six_charac_eq_m, how='inner', left_index=True, right_index=True)
    # # print(duplicates)

    # # # Eliminamos las muestras a utilizar del resto de muestras que no se analizaran
    final_samples = final_samples.drop(duplicates.index)

    return six_charac_eq_m, final_samples


def fourth_condition(final_samples):
    '''
    Esta funcion evalua que las muestras de las caracteristicas v2, v6, v7, v8, v10, INCLUYENDO v1
    sean exactamente igual a la moda de cada caracteristica
    '''
    # Tomando exactamente la moda de esas caracteristicas
    six_charac_eq_m1 = final_samples[(final_samples['v2'] == 56.3) &
                                     (final_samples['v6'] == 1) &
                                     (final_samples['v7'] == 2.1) &
                                     (final_samples['v8'] == 3.8) &
                                     (final_samples['v10'] == 23.8) &
                                     (final_samples['v1'] == 21.1)]

    # obtenemos 5 muestras que cumplen el requisito
    # six_charac_eq_m1.count()
    # print(six_charac_eq_m1)

    # # # Match de las muestras que tienen todas las caracteristicas de sustancias nocivas contra todas las muestras
    duplicates = pd.merge(final_samples, six_charac_eq_m1, how='inner', left_index=True, right_index=True)
    # # print(duplicates)

    # # # Eliminamos las muestras a utilizar del resto de muestras que no se analizaran
    final_samples = final_samples.drop(duplicates.index)

    return six_charac_eq_m1, final_samples


def fifth_condition(final_samples):
    '''
    Esta funcion evalua que las muestras de las caracteristicas v2, v6, v7, v8, v10, v1
    sean mayor igual a la moda de cada caracteristica
    '''
    # Tomando la moda mayor o igual a esta de esas caracteristicas
    six_charac_gt_m = final_samples[(final_samples['v2'] >= 56.3) &
                                    (final_samples['v6'] >= 1) &
                                    (final_samples['v7'] >= 2.1) &
                                    (final_samples['v8'] >= 3.8) &
                                    (final_samples['v10'] >= 23.8) &
                                    (final_samples['v1'] >= 21.1)]

    # obtenemos 11 muestras que cumplen el requisito
    # six_charac_gt_m.count()
    # print(six_charac_gt_m)

    # # Match de las muestras que tienen todas las caracteristicas de sustancias nocivas contra todas las muestras
    duplicates = pd.merge(final_samples, six_charac_gt_m, how='inner', left_index=True, right_index=True)
    # print(duplicates)

    # # Eliminamos las muestras a utilizar del resto de muestras que no se analizaran
    final_samples = final_samples.drop(duplicates.index)

    return six_charac_gt_m, final_samples


def sixth_condition(final_samples):
    '''
        Esta funcion evalua que las muestras de las caracteristicas v2, v6, v7, v8, v10
        sean mayor igual a la moda de cada caracteristica
    '''
    # Tomando la moda mayor o igual a esta de esas caracteristicas
    six_charac_gt_m1 = final_samples[(final_samples['v2'] >= 56.3) &
                                     (final_samples['v6'] >= 1) &
                                     (final_samples['v7'] >= 2.1) &
                                     (final_samples['v8'] >= 3.8) &
                                     (final_samples['v10'] >= 23.8)]

    # obtenemos 11 muestras que cumplen el requisito
    # six_charac_gt_m1.count()
    # print(six_charac_gt_m1)

    # # Match de las muestras que tienen todas las caracteristicas de sustancias nocivas contra todas las muestras
    duplicates = pd.merge(final_samples, six_charac_gt_m1, how='inner', left_index=True, right_index=True)
    # print(duplicates)

    # # Eliminamos las muestras a utilizar del resto de muestras que no se analizaran
    final_samples = final_samples.drop(duplicates.index)

    return six_charac_gt_m1
