import numpy as np
from .loader import load_model

_model = load_model("parkinsons_model.sav")

def predict_parkinsons(features: list[float]):
    data = np.array(features).reshape(1, -1)
    return int(_model.predict(data)[0])

