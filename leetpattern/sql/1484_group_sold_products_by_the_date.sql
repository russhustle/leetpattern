-- Task: For each sale date, report the number of distinct products sold and
-- their alphabetically sorted, comma-separated names; order results by date.
SELECT -- Return the daily product count and product list.
    sell_date, -- Identify the sale date.
    COUNT(DISTINCT product) AS num_sold, -- Count unique products per day.
    -- Deduplicate product names, sort them, and join them with commas.
    GROUP_CONCAT(DISTINCT product ORDER BY product SEPARATOR ',') AS products
FROM Activities -- Read the product sale records.
GROUP BY sell_date -- Combine all sales occurring on the same date.
ORDER BY sell_date; -- List dates chronologically.
