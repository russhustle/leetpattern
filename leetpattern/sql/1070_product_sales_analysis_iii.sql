SELECT
    s.product_id,
    s.year AS first_year,
    s.quantity,
    s.price
FROM Sales AS s
WHERE (s.product_id, s.year) IN (
    SELECT
        f.product_id,
        MIN(f.year) AS first_year
    FROM Sales AS f
    GROUP BY f.product_id
);
