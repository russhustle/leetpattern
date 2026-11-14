-- Task: For each month and country, report transaction counts and amounts,
-- including separate counts and amounts for approved transactions.
SELECT -- Calculate the requested monthly country-level metrics.
    country, -- Identify the transaction's country.
    DATE_FORMAT(trans_date, '%Y-%m') AS month, -- Extract the year and month.
    COUNT(*) AS trans_count, -- Count all transactions.
    -- COUNT ignores NULL, so only approved transactions contribute.
    COUNT(IF(state = 'approved', 1, NULL)) AS approved_count,
    SUM(amount) AS trans_total_amount, -- Sum all transaction amounts.
    -- Sum approved amounts while other transactions contribute zero.
    SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM transactions -- Include approved and declined transactions.
GROUP BY -- Compute metrics separately for each month and country.
    month, -- Group all dates within the same calendar month.
    country; -- Keep countries separate, including the NULL country group.
