import numpy as np
from .loader import load_model

_model = load_model("heart_disease_model.sav")

def predict_heart(
    age,
    sex,
    cp,
    trestbps,
    chol,
    fbs,
    restecg,
    thalach,
    exang,
    oldpeak,
    slope,
    ca,
    thal,
):
    features = [
        age, sex, cp, trestbps, chol, fbs, restecg,
        thalach, exang, oldpeak, slope, ca, thal
    ]

    data = np.array(features).reshape(1, -1)
    return int(_model.predict(data)[0])

