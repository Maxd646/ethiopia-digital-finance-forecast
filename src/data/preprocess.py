import pandas as pd

def preprocess_data(df):
    """Preprocess the data: dates, numeric, and string cleaning."""
    df = df.copy()

    # Convert date columns
    df["observation_date"] = pd.to_datetime(df["observation_date"], errors="coerce")
    for col in ["period_start", "period_end"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # Fill numeric missing values
    df["value_numeric"] = pd.to_numeric(df["value_numeric"], errors="coerce").fillna(0)

    # Trim string columns
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    return df
