-- Task: Find dates whose temperature is higher than the previous day's.
SELECT w1.id -- Return the ID of each warmer day's record.
FROM weather AS w1 -- Read the current day's weather.
-- Match the record from exactly one calendar day earlier.
LEFT JOIN weather AS w2 ON w1.recorddate - INTERVAL 1 DAY = w2.recorddate
WHERE -- Exclude missing previous days and non-increasing temperatures.
    w1.temperature > w2.temperature; -- Require a warmer current day.
