-- Task: Report each employee's unique ID and name, using NULL when no unique
-- ID has been assigned.
SELECT -- Return the mapped identifier and employee name.
    unique_id, -- Show the assigned unique ID, or NULL if missing.
    name -- Show the employee's name.
FROM employees -- Include employees even without a unique identifier.
-- Attach a unique ID when a matching employee mapping exists.
LEFT JOIN employeeuni ON employees.id = employeeuni.id;
