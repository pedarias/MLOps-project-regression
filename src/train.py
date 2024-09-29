# src/train.py

import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import mlflow
import mlflow.tensorflow

def build_and_compile_model(norm):
    model = keras.Sequential([
        norm,
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(1)
    ])

    model.compile(loss='mean_absolute_error',
                  optimizer=tf.keras.optimizers.Adam(0.001))
    return model

def train_model():
    # Carregar os dados
    train_dataset = pd.read_csv('data/train.csv')
    test_dataset = pd.read_csv('data/test.csv')

    # Separar features e labels
    train_features = train_dataset.copy()
    test_features = test_dataset.copy()

    train_labels = train_features.pop('MPG')
    test_labels = test_features.pop('MPG')

    # Normalização
    normalizer = tf.keras.layers.Normalization(axis=-1)
    normalizer.adapt(np.array(train_features))

    # Configurar o MLflow
    mlflow.tensorflow.autolog()

    with mlflow.start_run() as run:
        # Construir e compilar o modelo
        model = build_and_compile_model(normalizer)

        # Treinar o modelo
        history = model.fit(
            train_features,
            train_labels,
            validation_split=0.2,
            verbose=1,
            epochs=100
        )

        # Avaliar o modelo
        loss = model.evaluate(test_features, test_labels, verbose=1)
        print(f"Teste de perda (Mean Absolute Error): {loss}")

        # Salvar o modelo
        model.save('models/dnn_model.keras', include_optimizer=False)

        # Logar o modelo no MLflow
        mlflow.log_metric('test_loss', loss)

if __name__ == "__main__":
    train_model()
