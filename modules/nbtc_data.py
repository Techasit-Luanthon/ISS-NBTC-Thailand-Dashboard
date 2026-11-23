from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CSV = PROJECT_ROOT / "data" / "nbtc_sample.csv"
REQUIRED_COLUMNS = {"date", "topic", "value", "unit", "source_url"}

def validate_nbtc_csv(frame: pd.DataFrame):
    missing = REQUIRED_COLUMNS.difference(frame.columns)
    if missing:
        return False, "Missing required columns: " + ", ".join(sorted(missing))
    try:
        pd.to_numeric(frame["value"], errors="raise")
    except (ValueError, TypeError):
        return False, "The 'value' column must contain numeric values."
    return True, "CSV structure is valid."

def load_nbtc_data():
    if not DEFAULT_CSV.exists():
        return pd.DataFrame(columns=sorted(REQUIRED_COLUMNS))
    frame = pd.read_csv(DEFAULT_CSV)
    valid, message = validate_nbtc_csv(frame)
    if not valid:
        raise ValueError(message)
    return frame
