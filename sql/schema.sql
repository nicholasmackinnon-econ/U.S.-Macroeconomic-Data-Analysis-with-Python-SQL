CREATE TABLE IF NOT EXISTS series_metadata (
    series_id TEXT PRIMARY KEY,
    indicator_name TEXT NOT NULL,
    category TEXT,
    units TEXT,
    frequency TEXT,
    notes TEXT
);

CREATE TABLE IF NOT EXISTS macro_observations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    series_id TEXT NOT NULL,
    date TEXT NOT NULL,
    value REAL,
    FOREIGN KEY (series_id) REFERENCES series_metadata(series_id)
);
