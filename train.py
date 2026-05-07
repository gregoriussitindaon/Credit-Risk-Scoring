"""Training script."""
import joblib
from pathlib import Path
from sklearn.ensemble import RandomForestClassifier

from .data_loader import load_splits

MODELS_DIR = Path(__file__).parent / "models"
MODELS_DIR.mkdir(exist_ok=True)


def train_model():
    X_train, X_test, y_train, y_test = load_splits()
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, MODELS_DIR / "best_model.pkl")
    print(f"Model disimpan ke {MODELS_DIR / 'best_model.pkl'}")
    return model


if __name__ == "__main__":
    train_model()
