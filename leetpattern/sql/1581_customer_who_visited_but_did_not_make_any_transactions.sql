-- Task: Find customers with visits that had no transactions, and count those
-- transaction-free visits for each customer.

-- 1. Left join: keep visits without a matching transaction.
SELECT -- Return customers and their transaction-free visit counts.
    v.customer_id, -- Identify the customer.
    COUNT(v.visit_id) AS count_no_trans -- Count visits without transactions.
FROM visits AS v -- Include visits even when no transaction exists.
LEFT JOIN transactions AS t ON v.visit_id = t.visit_id -- Attach transactions.
WHERE -- Identify visits with no matching transaction.
    t.transaction_id IS NULL -- Exclude visits that produced transactions.
GROUP BY -- Count the remaining visits per customer.
    v.customer_id; -- Return one row per qualifying customer.

-- 2. Subquery: exclude visits appearing in the transaction table.
SELECT -- Return the same customer-level counts.
    customer_id, -- Identify the customer.
    COUNT(DISTINCT visit_id) AS count_no_trans -- Count unique eligible visits.
FROM visits -- Read all recorded customer visits.
WHERE -- Remove visits with any transaction.
    visit_id NOT IN ( -- Compare against all transaction-linked visits.
        SELECT visit_id -- Return IDs of visits that produced transactions.
        FROM transactions -- Collect visits referenced by transactions.
    ) -- Finish the exclusion list.
GROUP BY -- Aggregate the transaction-free visits per customer.
    customer_id; -- Produce one count per qualifying customer.
