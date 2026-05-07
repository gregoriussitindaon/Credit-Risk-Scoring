"""Evaluation utilities."""
import joblib
from pathlib import Path

from .data_loader import load_splits

MODELS_DIR = Path(__file__).parent / "models"


def evaluate():
    model = joblib.load(MODELS_DIR / "best_model.pkl")
    try:
        X_train, X_test, y_train, y_test = load_splits()
        score = model.score(X_test, y_test)
        print(f"Test score: {score:.4f}")
        return score
    except FileNotFoundError:
        print("Splits tidak tersedia (proyek non-supervised).")
        return None


if __name__ == "__main__":
    evaluate()
