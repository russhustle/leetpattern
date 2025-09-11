SELECT
    country,
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    COUNT(*) AS trans_count,
    COUNT(IF(state = 'approved', 1, NULL)) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state = 'approved', amount, 0)) AS approved_total_amount
FROM
    transactions
GROUP BY
    month,
    country;
