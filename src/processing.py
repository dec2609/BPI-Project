"""Data preprocessing functions."""
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned = cleaned.drop_duplicates()
    return cleaned
