-- Task: Report each employee's primary department, or their only department
-- when they belong to just one.
SELECT -- Return each employee's chosen department.
    e.employee_id, -- Identify the employee.
    e.department_id -- Identify their primary or sole department.
FROM Employee AS e -- Read employee-department memberships.
WHERE -- Accept either an explicit primary flag or sole membership.
    e.primary_flag = 'Y' -- Include departments explicitly marked primary.
    OR e.employee_id IN ( -- Also include employees with just one department.
        SELECT d.employee_id FROM Employee AS d -- Examine all memberships.
        GROUP BY d.employee_id -- Count departments for each employee.
        HAVING COUNT(*) = 1 -- Keep employees belonging to exactly one.
    ); -- Finish the sole-department lookup.
