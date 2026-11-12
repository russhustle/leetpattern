WITH ranked AS (
    SELECT
        departmentId,
        name,
        salary,
        DENSE_RANK()
            OVER (PARTITION BY departmentId ORDER BY salary DESC)
            AS salary_rank
    FROM Employee
)

SELECT
    d.name AS Department,
    r.name AS Employee,
    r.salary AS Salary -- noqa: AL09
FROM ranked AS r
INNER JOIN Department AS d ON r.departmentId = d.id
WHERE r.salary_rank <= 3;
