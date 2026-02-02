import numpy as np
from .loader import load_model

_model = load_model("breast_cancer_model.sav")

def predict_breast_cancer(features: list[float]):
    data = np.array(features).reshape(1, -1)
    return int(_model.predict(data)[0])

