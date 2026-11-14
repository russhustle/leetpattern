-- Task: Report the product name, year, and price for each sale.
SELECT -- Return the requested sale details.
    p.product_name, -- Get the product's readable name.
    s.year, -- Show the year of the sale.
    s.price -- Show the sale price per unit.
FROM sales AS s -- Keep each sale as a separate output row.
LEFT JOIN product AS p ON s.product_id = p.product_id; -- Look up product names.
