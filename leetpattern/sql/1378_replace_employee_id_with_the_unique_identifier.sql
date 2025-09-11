-- Replace employee id with the unique identifier
SELECT
    unique_id,
    name
FROM
    employees
LEFT JOIN employeeuni ON employees.id = employeeuni.id;
