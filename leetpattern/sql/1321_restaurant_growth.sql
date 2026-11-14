-- Task: Report each full seven-day window's total customer spending and
-- average daily spending, rounded to two decimals and ordered by date.
SELECT -- Return the ending date and its seven-day spending metrics.
    dates.visited_on, -- Identify the last day of the window.
    SUM(c.amount) AS amount, -- Add all spending within the window.
    ROUND(SUM(c.amount) / 7, 2) AS average_amount -- Average across seven days.
FROM (SELECT DISTINCT visited_on FROM Customer) AS dates -- Use one row per day.
INNER JOIN Customer AS c -- Attach customer spending in each date's window.
    ON -- Match the current day and its previous six days.
        c.visited_on BETWEEN DATE_SUB( -- Calculate the window's starting date.
            dates.visited_on, INTERVAL 6 DAY -- Start six days before this date.
        ) AND dates.visited_on -- Include spending through the ending date.
WHERE -- Skip dates that cannot yet have a complete seven-day window.
    dates.visited_on -- Compare each candidate ending date with the first date.
    -- The earliest full window ends six days after the first customer visit.
    >= DATE_ADD((SELECT MIN(visited_on) FROM Customer), INTERVAL 6 DAY)
GROUP BY dates.visited_on -- Calculate one result for each ending date.
ORDER BY dates.visited_on; -- List windows chronologically.
