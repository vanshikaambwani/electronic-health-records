import pickle
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_DIR = BASE_DIR / "models"

def load_model(filename: str):
    with open(MODEL_DIR / filename, "rb") as f:
        return pickle.load(f)

