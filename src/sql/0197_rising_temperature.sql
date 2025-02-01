SELECT w1.id
FROM
    weather AS w1
LEFT JOIN weather AS w2 ON w1.recorddate - INTERVAL 1 DAY = w2.recorddate
WHERE
    w1.temperature > w2.temperature;
