SELECT
    dates.visited_on,
    SUM(c.amount) AS amount,
    ROUND(SUM(c.amount) / 7, 2) AS average_amount
FROM (SELECT DISTINCT visited_on FROM Customer) AS dates
INNER JOIN Customer AS c
    ON
        c.visited_on BETWEEN DATE_SUB(
            dates.visited_on, INTERVAL 6 DAY
        ) AND dates.visited_on
WHERE
    dates.visited_on
    >= DATE_ADD((SELECT MIN(visited_on) FROM Customer), INTERVAL 6 DAY)
GROUP BY dates.visited_on
ORDER BY dates.visited_on;
