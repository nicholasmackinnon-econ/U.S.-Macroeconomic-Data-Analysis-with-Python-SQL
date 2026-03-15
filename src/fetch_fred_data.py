import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FRED_API_KEY")

BASE_URL = "https://api.stlouisfed.org/fred/series/observations"

SERIES = {
    "GDP": "Gross Domestic Product",
    "CPIAUCSL": "Consumer Price Index",
    "UNRATE": "Unemployment Rate",
    "FEDFUNDS": "Federal Funds Rate"
}

def fetch_series(series_id):
    params = {
        "series_id": series_id,
        "api_key": API_KEY,
        "file_type": "json"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    observations = data["observations"]

    df = pd.DataFrame(observations)
    df = df[["date", "value"]]

    df["series_id"] = series_id
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df["date"] = pd.to_datetime(df["date"])

    return df


def main():

    all_data = []

    for series_id in SERIES:
        print(f"Downloading {SERIES[series_id]}...")
        df = fetch_series(series_id)
        all_data.append(df)

    combined = pd.concat(all_data)

    combined.to_csv("data/exports/macro_observations.csv", index=False)

    print("Data saved to data/exports/macro_observations.csv")


if __name__ == "__main__":
    main()
    