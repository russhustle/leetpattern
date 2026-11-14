-- Task: Return the second-highest distinct salary, or NULL if none exists.
-- MAX returns the largest remaining salary, or NULL when no rows remain.
SELECT MAX(e.salary) AS SecondHighestSalary
FROM Employee AS e -- Read employee salaries.
-- Exclude the highest salary to leave only lower, distinct salary levels.
WHERE e.salary < (SELECT MAX(x.salary) FROM Employee AS x); -- noqa: RF03
