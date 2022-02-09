import os
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import models,utils
import pandas as pd
from tensorflow.keras.models import load_model

current_path = os.getcwd()

# Load the titanic model
model = load_model(os.path.join(current_path, "titanic_model"))

# Load the scaler
with open(os.path.join(current_path, "static/scaler.pkl"), "rb") as handle:
    sc = pickle.load(handle)

# Function that predicts if survived or not
def predict_survival(title, pclass, fsize, sex, embarked, age, fare):
    data_ = {
        "Pclass": [pclass],
        "FSize": [fsize],
        "Sex_male": [sex],
        "Emb_Q": [0],
        "Emb_S": [0],
        "Age_Children": [0],
        "Age_Teen": [0],
        "Age_Student": [0],
        "Age_Young": [0],
        "Age_Adult": [0],
        "Age_Senior": [0],
        "Fare_quart_1": [0],
        "Fare_quart_2": [0],
        "Fare_quart_3": [0],
        "Fare_quart_4": [0],
        "Prefix_Miss": [0],
        "Prefix_Mr": [0],
        "Prefix_Mrs": [0],
        "Prefix_Officer": [0],
        "Prefix_Royalty": [0],
    }
    df = pd.DataFrame(data=data_)

    if title == 1:
        df["Prefix_Miss"] = 1
    elif title == 2:
        df["Prefix_Mr"] = 1
    elif title == 3:
        df["Prefix_Mrs"] = 1
    elif title == 4:
        df["Prefix_Officer"] = 1
    else:
        df["Prefix_Royalty"] = 1

    if embarked == 1:
        df["Emb_Q"] = 1
    elif embarked == 2:
        df["Emb_S"] = 1

    if fare == 1:
        df["Fare_quart_1"] = 1
    elif fare == 2:
        df["Fare_quart_2"] = 1
    elif fare == 3:
        df["Fare_quart_3"] = 1
    else:
        df["Fare_quart_4"] = 1

    if age == 1:
        df["Age_Children"] = 1
    elif age == 2:
        df["Age_Teen"] = 1
    elif age == 3:
        df["Age_Student"] = 1
    elif age == 4:
        df["Age_Young"] = 1
    elif age == 5:
        df["Age_Adult"] = 1
    else:
        df["Age_Senior"] = 1

    df = df.values
    df = sc.transform(df)

    pred = np.around(model.predict(df))

    return pred.astype(int)
