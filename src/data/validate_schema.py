REQUIRED_COLUMNS = [
    "record_id",
    "record_type",
    "pillar",
    "indicator",
    "indicator_code",
    "value_numeric",
    "observation_date",
    "category",
    "source_name",
    "source_url",
    "confidence"
]

VALID_RECORD_TYPES = ["observation", "event", "impact_link", "target"]

def validate_schema(df):
    """Validate required columns and record_type."""
    df.columns = df.columns.str.strip().str.lower()
    required = [col.lower() for col in REQUIRED_COLUMNS]

    missing_cols = set(required) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    invalid_types = df.loc[~df["record_type"].isin(VALID_RECORD_TYPES), "record_type"].unique()
    if len(invalid_types) > 0:
        raise ValueError(f"Invalid record_type found: {invalid_types}")
