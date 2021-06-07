import os
import pandas as pd
from src import config
from src.feature_processing import feature_process
from src.statistical_analysis import exploration_data


if __name__=="__main__":
    # - Leer archivos csv
    veneno = pd.read_csv(config.VENENO_DATA)
    sustancias_diversas = pd.read_csv(config.SUSTANCIAS_DATA)

    veneno,sustancias_diversas = feature_process(veneno, sustancias_diversas)

    exploration_data(veneno,sustancias_diversas)
