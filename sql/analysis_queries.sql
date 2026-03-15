-- 1. Count observations by series
SELECT
    series_id,
    COUNT(*) AS observation_count
FROM macro_observations
GROUP BY series_id
ORDER BY series_id;

-- 2. Date range for each series
SELECT
    series_id,
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM macro_observations
GROUP BY series_id
ORDER BY series_id;

-- 3. Latest value for each indicator
SELECT m.series_id, m.date, m.value
FROM macro_observations m
JOIN (
    SELECT series_id, MAX(date) AS max_date
    FROM macro_observations
    GROUP BY series_id
) latest
ON m.series_id = latest.series_id
AND m.date = latest.max_date
ORDER BY m.series_id;
