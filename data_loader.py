import pandas as pd

DATA_FILE = "dataset/ML-Dataset.csv"


def load_dataset():
    df = pd.read_csv(DATA_FILE)
    return df.to_dict(orient="records")