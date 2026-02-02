import numpy as np
from .loader import load_model

_model = load_model("diabetes_model_new.sav")

def predict_diabetes(
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    dpf,
    age,
):
    features = [
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        dpf,
        age,
    ]

    data = np.array(features).reshape(1, -1)
    return int(_model.predict(data)[0])

