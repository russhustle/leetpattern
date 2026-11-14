-- Task: Find employees earning a top-three distinct salary in their department.
WITH ranked AS ( -- Rank employees within each department.
    SELECT -- Keep employee details alongside their salary rank.
        departmentId, -- Identify the employee's department.
        name, -- Keep the employee's name.
        salary, -- Keep the employee's salary.
        DENSE_RANK() -- Give equal salaries the same rank, without gaps.
            -- Restart ranking per department, with the highest salary first.
            OVER (PARTITION BY departmentId ORDER BY salary DESC)
            AS salary_rank -- Name the calculated rank.
    FROM Employee -- Read all employees.
) -- Finish the ranked employee result.

SELECT -- Return the requested department, employee, and salary columns.
    d.name AS Department, -- Show the department's name.
    r.name AS Employee, -- Show the employee's name.
    -- Show the employee's salary under the required output name.
    r.salary AS Salary -- noqa: AL09
FROM ranked AS r -- Use the ranked employees.
INNER JOIN Department AS d ON r.departmentId = d.id -- Attach department names.
WHERE r.salary_rank <= 3; -- Include ties in the top three salary levels.
