# app.py

import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import tensorflow as tf
from tensorflow import keras

app = FastAPI()

# Carregar o modelo
model = keras.models.load_model('models/dnn_model.keras')

# Definir o modelo de dados de entrada
class CarFeatures(BaseModel):
    Cylinders: int
    Displacement: float
    Horsepower: float
    Weight: float
    Acceleration: float
    Model_Year: int
    USA: int = 0
    Europe: int = 0
    Japan: int = 0

#NOrm ja esta definido no modelo
# Normalização (usando os mesmos parâmetros do treinamento)
#normalizer = tf.keras.layers.Normalization(axis=-1)
# Carregue os parâmetros de normalização a partir dos dados de treinamento
#train_features = pd.read_csv('data/train.csv').drop('MPG', axis=1)
#normalizer.adapt(np.array(train_features))

# Add a root route
@app.get("/")
async def read_root():
    return {"message": "Welcome to the MPG Prediction API"}

@app.post("/predict")
def predict_mpg(features: CarFeatures):
    # Converter os dados de entrada em um DataFrame
    input_df = pd.DataFrame([features.dict()])
    # Normalizar os dados
    #input_normalized = normalizer(np.array(input_df))
    # Fazer a previsão
    prediction = model.predict(input_df)
    mpg = float(prediction[0][0])  # Converter para float nativo
    return {"MPG": mpg}
