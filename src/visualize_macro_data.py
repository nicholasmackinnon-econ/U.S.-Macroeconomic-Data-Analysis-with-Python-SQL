import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DB_PATH = "data/raw/macroeconomic_data.db"
IMG_DIR = Path("images")
IMG_DIR.mkdir(exist_ok=True)

def load_series(series_id):
    conn = sqlite3.connect(DB_PATH)

    query = f"""
    SELECT date, value
    FROM macro_observations
    WHERE series_id = '{series_id}'
    ORDER BY date
    """

    df = pd.read_sql_query(query, conn, parse_dates=["date"])
    conn.close()

    return df


def save_chart(df, title, ylabel, filename):

    plt.figure(figsize=(10,5))
    plt.plot(df["date"], df["value"])

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel(ylabel)

    plt.tight_layout()
    plt.savefig(IMG_DIR / filename)
    plt.close()


def main():

    gdp = load_series("GDP")
    cpi = load_series("CPIAUCSL")
    unrate = load_series("UNRATE")
    fedfunds = load_series("FEDFUNDS")

    save_chart(gdp, "U.S. GDP Over Time", "Billions of Dollars", "gdp_trend.png")
    save_chart(cpi, "Consumer Price Index (CPI)", "Index", "cpi_trend.png")
    save_chart(unrate, "U.S. Unemployment Rate", "Percent", "unemployment_trend.png")
    save_chart(fedfunds, "Federal Funds Rate", "Percent", "fedfunds_trend.png")

    print("Charts saved to images/ folder")


if __name__ == "__main__":
    main()
    