-- Task: Find customers who bought every product listed in the Product table.
SELECT customer_id -- Return qualifying customer IDs.
FROM Customer -- Read customer purchases.
GROUP BY customer_id -- Evaluate each customer's purchases together.
-- Compare unique purchased products with the total number of products.
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);
