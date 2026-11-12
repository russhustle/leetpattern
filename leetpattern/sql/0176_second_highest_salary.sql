SELECT MAX(e.salary) AS SecondHighestSalary
FROM Employee AS e
WHERE e.salary < (SELECT MAX(x.salary) FROM Employee AS x); -- noqa: RF03
