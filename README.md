# U.S. Macroeconomic Data Analysis (Python + SQL)

## Overview

This project analyzes key U.S. macroeconomic indicators using data from the Federal Reserve Economic Data (FRED) database.

The analysis integrates Python, SQL, and SQLite to build a complete data workflow that includes data ingestion, storage, querying, and visualization.

The goal of this project is to demonstrate how economic data can be transformed into insights using modern data analysis tools.

---

## Indicators Analyzed

The project examines four major macroeconomic indicators:

- Gross Domestic Product (GDP) – overall economic output
- Consumer Price Index (CPI) – inflation indicator
- Unemployment Rate (UNRATE) – labor market conditions
- Federal Funds Rate (FEDFUNDS) – monetary policy instrument

These indicators provide a broad view of the U.S. economy and its response to economic cycles and policy changes.

---

## Tools and Technologies

This project uses the following tools:

- Python  
- pandas  
- Matplotlib  
- SQLite  
- SQL  
- FRED API  

The combination of Python and SQL allows the project to demonstrate both data engineering workflows and analytical techniques.

---

## Project Workflow

The analysis follows a structured data pipeline:

FRED API → Python → CSV → SQLite → SQL Analysis → Python Visualization

Steps performed in the workflow:

1. Retrieve macroeconomic time-series data from the FRED API.
2. Store the data in CSV format.
3. Load the data into a SQLite database.
4. Perform SQL queries to validate and analyze the dataset.
5. Load queried data into Python for visualization.
6. Interpret macroeconomic trends using charts and summary analysis.

---

## Database Structure

The SQLite database contains one main table:

macro_observations

Columns:

date – observation date  
value – indicator value  
series_id – identifier for the macroeconomic series

Each row represents a time-series observation for one macroeconomic indicator.

---

## Data Validation

SQL queries were used to confirm that the dataset loaded correctly into SQLite. These checks verified:

- number of observations per indicator
- time coverage for each series
- correct database structure

This step ensures the reliability of the dataset before performing analysis.

---

## Analysis

The project performs several types of analysis:

### Time-Series Visualization

Python visualizations illustrate long-term trends in:

- GDP growth
- inflation dynamics
- unemployment cycles
- changes in interest rates

### Labor Market Analysis

Unemployment data is aggregated by decade to illustrate changes in labor market conditions over time.

### Monetary Policy Analysis

The Federal Funds Rate series shows how the Federal Reserve adjusts interest rates in response to inflation and economic conditions.

---

## Key Insights

Several macroeconomic patterns emerge from the analysis:

- GDP shows sustained long-run growth despite economic recessions.
- CPI illustrates long-term inflation and recent post-pandemic price increases.
- Unemployment fluctuates with the business cycle.
- Federal Reserve interest rate policy responds to inflation and economic instability.

These indicators together illustrate how economic growth, labor markets, inflation, and monetary policy interact within the U.S. economy.

---

## Project Structure

U.S.-Macroeconomic-Data-Analysis-with-Python-SQL

data/  
    raw/  
        macroeconomic_data.db  
        macro_observations.csv  

notebook/  
    macroeconomic_analysis.ipynb  

sql/  
    analysis_queries.sql  

src/  
    test_fred_connection.py  

images/  
    gdp_trend.png  
    cpi_trend.png  
    unemployment_trend.png  
    fedfunds_trend.png  

requirements.txt  
README.md  

---

## How to Run the Project

1. Clone the repository

git clone https://github.com/nicholasmackinnon-econ/U.S.-Macroeconomic-Data-Analysis-with-Python-SQL.git

2. Install required libraries

pip install -r requirements.txt

3. Open the Jupyter notebook

notebook/macroeconomic_analysis.ipynb

4. Run all cells to reproduce the analysis and visualizations.

---

## Purpose of the Project

This project was created as part of a data analytics and economics portfolio to demonstrate skills in:

- economic data analysis
- SQL querying
- Python data workflows
- data visualization
- macroeconomic interpretation

---

## Author

Nicholas Mackinnon  
Economics Student
