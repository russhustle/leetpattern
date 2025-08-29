SELECT e2.name
FROM
    employee AS e1
INNER JOIN employee AS e2 ON e1.managerid = e2.id
GROUP BY
    e2.id,
    e2.name
HAVING
    COUNT(e1.id) >= 5;
