-- Task: Report every product's price on 2019-08-16, using 10 before its first
-- price change.
SELECT -- Return each product and its effective price.
    p.product_id, -- Identify the product.
    COALESCE(c.new_price, 10) AS price -- Use 10 if no earlier price exists.
FROM (SELECT DISTINCT product_id FROM Products) AS p -- Include every product.
LEFT JOIN Products AS c -- Look up the effective price without losing products.
    ON -- Match the product's most recent change on or before the target date.
        p.product_id = c.product_id -- Require the same product.
        AND c.change_date = ( -- Select only its last eligible change.
            -- Find this product's latest eligible price-change date.
            SELECT MAX(history.change_date) FROM Products AS history
            WHERE -- Limit the price history to this product and target date.
                history.product_id = p.product_id -- Match the outer product.
                AND history.change_date <= '2019-08-16' -- Ignore later changes.
        ); -- Finish the latest-change lookup.
