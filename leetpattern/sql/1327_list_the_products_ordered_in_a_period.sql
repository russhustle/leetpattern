-- Task: Report products ordered at least 100 units in February 2020,
-- including their product names and total ordered units.
SELECT -- Return the product name and February order volume.
    p.product_name, -- Show the product's readable name.
    SUM(o.unit) AS unit -- Add all units ordered in the filtered period.
FROM Products AS p -- Read product information.
INNER JOIN Orders AS o ON p.product_id = o.product_id -- Attach product orders.
-- Include all February dates and exclude March onward.
WHERE o.order_date >= '2020-02-01' AND o.order_date < '2020-03-01'
GROUP BY p.product_id, p.product_name -- Total units per product.
HAVING SUM(o.unit) >= 100; -- Keep products meeting the 100-unit threshold.
