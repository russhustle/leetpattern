-- Task: For each query name, report average rating/position quality and the
-- percentage of ratings below 3, both rounded to two decimal places.
SELECT -- Calculate both metrics for each query name.
    query_name, -- Identify the query.
    ROUND(AVG(rating / POSITION), 2) AS quality, -- Average rating/position.
    -- Divide the count of poor ratings by all rows and convert to a percentage.
    ROUND(SUM(IF(rating < 3, 1, 0)) / COUNT(*) * 100, 2)
        AS poor_query_percentage -- Name the rounded poor-query percentage.
FROM queries -- Read all query evaluations.
WHERE -- Exclude records without a query name.
    query_name IS NOT NULL -- Require a named query.
GROUP BY -- Aggregate repeated evaluations of the same query.
    query_name; -- Produce one row per query name.
