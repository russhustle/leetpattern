-- 1.
SELECT
    e.name,
    b.bonus
FROM
    employee AS e
LEFT JOIN bonus AS b ON e.empid = b.empid
WHERE
    b.bonus < 1000
    OR b.bonus IS NULL;

-- 2.
SELECT
    e.name,
    b.bonus
FROM
    employee AS e
LEFT JOIN bonus AS b ON e.empid = b.empid
WHERE
    COALESCE(b.bonus, 0) < 1000;
