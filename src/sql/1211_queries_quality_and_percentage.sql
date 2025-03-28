SELECT
    query_name,
    ROUND(AVG(rating / POSITION), 2) AS quality,
    ROUND(SUM(IF(rating < 3, 1, 0)) / COUNT(*) * 100, 2)
        AS poor_query_percentage
FROM
    queries
WHERE
    query_name IS NOT NULL
GROUP BY
    query_name;
