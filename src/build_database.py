import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = "data/raw/macroeconomic_data.db"
CSV_PATH = "data/exports/macro_observations.csv"

SERIES_METADATA = [
    ("GDP", "Gross Domestic Product", "Output", "Billions of Dollars", "Quarterly", "US GDP"),
    ("CPIAUCSL", "Consumer Price Index", "Prices", "Index 1982-1984=100", "Monthly", "CPI for All Urban Consumers"),
    ("UNRATE", "Unemployment Rate", "Labor Market", "Percent", "Monthly", "Civilian Unemployment Rate"),
    ("FEDFUNDS", "Federal Funds Rate", "Monetary Policy", "Percent", "Monthly", "Effective Federal Funds Rate")
]

def run_schema(conn, schema_path="sql/schema.sql"):
    with open(schema_path, "r", encoding="utf-8") as f:
        conn.executescript(f.read())

def main():
    Path("data/raw").mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    run_schema(conn)

    meta_df = pd.DataFrame(
        SERIES_METADATA,
        columns=["series_id", "indicator_name", "category", "units", "frequency", "notes"]
    )
    meta_df.to_sql("series_metadata", conn, if_exists="replace", index=False)

    obs_df = pd.read_csv(CSV_PATH)
    obs_df.to_sql("macro_observations", conn, if_exists="replace", index=False)

    conn.execute("CREATE INDEX IF NOT EXISTS idx_series_date ON macro_observations(series_id, date);")

    conn.commit()
    conn.close()

    print("Database built successfully.")
    print(f"Database saved to {DB_PATH}")

if __name__ == "__main__":
    main()
    