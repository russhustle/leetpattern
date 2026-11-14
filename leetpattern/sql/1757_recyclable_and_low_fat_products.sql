-- Task: Find products that are both low-fat and recyclable.
SELECT product_id -- Return the IDs of qualifying products.
FROM products -- Read the product catalog.
WHERE -- Require both product properties.
    low_fats = 'Y' -- Keep products marked low-fat.
    AND recyclable = 'Y'; -- Also require them to be recyclable.
