SELECT
    s.user_id,
    ROUND(
        SUM(IF(c.action = 'confirmed', 1, 0)) / COUNT(*),
        2
    ) AS confirmation_rate
FROM
    signups AS s
LEFT JOIN confirmations AS c ON s.user_id = c.user_id
GROUP BY
    s.user_id;
