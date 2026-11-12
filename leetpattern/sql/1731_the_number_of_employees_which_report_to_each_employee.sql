SELECT
    m.employee_id,
    m.name,
    COUNT(*) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
FROM Employees AS m
INNER JOIN Employees AS e ON m.employee_id = e.reports_to
GROUP BY m.employee_id, m.name
ORDER BY m.employee_id;
