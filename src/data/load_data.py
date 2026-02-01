import pandas as pd
from pathlib import Path

from pathlib import Path

# Set DATA_DIR to the root data folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # Go up 3 levels to repo root
DATA_DIR = PROJECT_ROOT / "data"


def load_raw_data():
    data = pd.read_csv(DATA_DIR / "raw" / "ethiopia_fi_unified_data.csv")
    ref = pd.read_csv(DATA_DIR / "raw" / "reference_codes.csv")
    return data, ref

def save_interim_data(df, filename="ethiopia_fi_enriched.csv"):
    """Save dataframe to the processed folder."""
    processed_dir = DATA_DIR / "processed"
    processed_dir.mkdir(exist_ok=True)  # create folder if not exists
    file_path = processed_dir / filename
    df.to_csv(file_path, index=False)
    print(f"Saved interim data to {file_path}")
