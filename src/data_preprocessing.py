# src/data_preprocessing.py

import pandas as pd
from sklearn.model_selection import train_test_split

def preprocess_data(input_path, train_path, test_path):
    dataset = pd.read_csv(input_path)
    dataset = dataset.dropna()

    # Transformar a coluna 'Origin' em variáveis dummy
    dataset['Origin'] = dataset['Origin'].map({1: 'USA', 2: 'Europe', 3: 'Japan'})
    dataset = pd.get_dummies(dataset, columns=['Origin'], prefix='', prefix_sep='')

    # Dividir em conjuntos de treinamento e teste
    train_dataset, test_dataset = train_test_split(dataset, test_size=0.2, random_state=42)

    # Salvar conjuntos
    train_dataset.to_csv(train_path, index=False)
    test_dataset.to_csv(test_path, index=False)
    print(f"Dados pré-processados e salvos em {train_path} e {test_path}")

if __name__ == "__main__":
    preprocess_data('data/auto-mpg.csv', 'data/train.csv', 'data/test.csv')
