"""Data loading utilities."""
from pathlib import Path
import pandas as pd

DATA_DIR = Path(__file__).parent.parent / "data"


def load_raw():
    raw = DATA_DIR / "raw"
    csv_files = list(raw.glob("*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"Tidak ada CSV di {raw}")
    return pd.read_csv(csv_files[0])


def load_processed():
    return pd.read_csv(DATA_DIR / "processed" / "features.csv")


def load_splits():
    proc = DATA_DIR / "processed"
    return (
        pd.read_csv(proc / "X_train.csv"),
        pd.read_csv(proc / "X_test.csv"),
        pd.read_csv(proc / "y_train.csv").iloc[:, 0],
        pd.read_csv(proc / "y_test.csv").iloc[:, 0],
    )
