-- Select product name, year, and price from Sales and Product tables
SELECT
    p.product_name,
    s.year,
    s.price
FROM
    sales AS s
INNER JOIN
    product AS p
    ON
        s.product_id = p.product_id;
