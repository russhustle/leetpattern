SELECT
    r.contest_id,
    ROUND(
        COUNT(DISTINCT r.user_id) / COUNT(DISTINCT u.user_id) * 100,
        2
    ) AS percentage
FROM
    users AS u
CROSS JOIN register AS r
GROUP BY
    r.contest_id
ORDER BY
    percentage DESC,
    contest_id ASC
