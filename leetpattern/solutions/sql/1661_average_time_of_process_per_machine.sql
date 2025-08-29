SELECT
    a1.machine_id,
    ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
    -- ROUND(SUM(a2.timestamp - a1.timestamp) / COUNT(*), 3) AS processing_time
FROM
    activity AS a1
INNER JOIN activity AS a2
    ON
        a1.machine_id = a2.machine_id
        AND a1.process_id = a2.process_id
        AND a1.timestamp < a2.timestamp
GROUP BY
    a1.machine_id;
