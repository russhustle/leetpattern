-- Task: Report each product's sales in its first year, including quantity
-- and price; preserve all sales rows from that earliest year.
SELECT -- Return the earliest-year sale details.
    s.product_id, -- Identify the product.
    s.year AS first_year, -- Label the sale year as the product's first year.
    s.quantity, -- Keep the quantity from this sale row.
    s.price -- Keep the price from this sale row.
FROM Sales AS s -- Examine every sale without combining its details.
WHERE (s.product_id, s.year) IN ( -- Keep only product/first-year pairs.
    SELECT -- Find the earliest year for each product.
        f.product_id, -- Identify the product being grouped.
        MIN(f.year) AS first_year -- Choose its minimum sale year.
    FROM Sales AS f -- Read all sales to find first years.
    GROUP BY f.product_id -- Calculate one first year per product.
); -- Match all sale rows belonging to those first years.
