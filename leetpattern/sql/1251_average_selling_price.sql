-- Task: Report each product's unit-weighted average selling price, rounded
-- to two decimal places; return zero for products without sales.
SELECT -- Return each product and its average selling price.
    p.product_id, -- Identify the product.
    COALESCE( -- Replace a missing average with zero.
        ROUND(SUM(p.price * u.units) / SUM(u.units), 2), -- Revenue / units.
        0 -- Use zero when no matching sales exist.
    ) AS average_price -- Name the rounded, defaulted result.
FROM prices AS p -- Include price records even when no units were sold.
LEFT JOIN unitssold AS u -- Attach sales to the applicable price interval.
    ON -- Match both product identity and purchase date.
        p.product_id = u.product_id -- Require the same product.
        -- Use the price effective on the purchase date, including endpoints.
        AND u.purchase_date BETWEEN p.start_date AND p.end_date
GROUP BY -- Combine all price intervals and sales for each product.
    p.product_id; -- Produce one weighted average per product.
