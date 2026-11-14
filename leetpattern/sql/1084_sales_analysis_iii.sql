-- Task: Report products sold only between 2019-01-01 and 2019-03-31 inclusive.
-- Products with any sale outside that interval, or no sales, do not qualify.
SELECT -- Return qualifying product IDs and names.
    s.product_id, -- Identify the sold product.
    p.product_name -- Show the product's name.
FROM Sales AS s -- Start with sales so unsold products are excluded.
JOIN Product AS p ON s.product_id = p.product_id -- Attach product names.
GROUP BY s.product_id, p.product_name -- Examine all sales of each product.
HAVING MIN(s.sale_date) >= '2019-01-01' -- Exclude any sale before Q1.
   AND MAX(s.sale_date) <= '2019-03-31'; -- Exclude any sale after Q1.
