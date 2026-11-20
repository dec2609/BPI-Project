"""Data ingestion utilities."""
from pathlib import Path
import pandas as pd
from src.config import RAW_DATA_DIR

def load_dataset(filename: str, **kwargs) -> pd.DataFrame:
    file_path = RAW_DATA_DIR / filename
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if file_path.suffix.lower() == ".csv":
        return pd.read_csv(file_path, **kwargs)
    elif file_path.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(file_path, **kwargs)
    elif file_path.suffix.lower() == ".parquet":
        return pd.read_parquet(file_path, **kwargs)
    else:
        raise ValueError(f"Unsupported format: {file_path.suffix}")
