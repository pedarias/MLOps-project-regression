# src/data_ingestion.py

import pandas as pd
import os

def download_data():
    url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'
    column_names = [
        'MPG', 'Cylinders', 'Displacement', 'Horsepower', 'Weight',
        'Acceleration', 'Model Year', 'Origin'
    ]
    dataset = pd.read_csv(
        url, names=column_names,
        na_values='?', comment='\t',
        sep=' ', skipinitialspace=True
    )
    os.makedirs('data', exist_ok=True)
    dataset.to_csv('data/auto-mpg.csv', index=False)
    print("Dados baixados e salvos em data/auto-mpg.csv")

if __name__ == "__main__":
    download_data()
