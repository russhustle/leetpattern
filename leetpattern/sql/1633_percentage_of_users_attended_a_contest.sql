SELECT
    r.contest_id,
    ROUND(
        COUNT(DISTINCT r.user_id) * 100.0 / (SELECT COUNT(*) FROM users),
        2
    ) AS percentage
FROM
    register AS r
GROUP BY
    r.contest_id
ORDER BY
    percentage DESC,
    contest_id ASC
