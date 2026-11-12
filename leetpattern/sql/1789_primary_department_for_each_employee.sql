SELECT
    e.employee_id,
    e.department_id
FROM Employee AS e
WHERE
    e.primary_flag = 'Y'
    OR e.employee_id IN (
        SELECT d.employee_id FROM Employee AS d
        GROUP BY d.employee_id
        HAVING COUNT(*) = 1
    );
