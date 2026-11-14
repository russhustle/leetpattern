-- Task: Report the names of managers with at least five direct reports.
SELECT e2.name -- Return each qualifying manager's name.
FROM employee AS e1 -- Represent employees who report to a manager.
INNER JOIN employee AS e2 ON e1.managerid = e2.id -- Find each report's manager.
GROUP BY -- Count direct reports separately for each manager.
    e2.id, -- Distinguish managers even when names match.
    e2.name -- Keep the manager's name available for output.
HAVING -- Filter managers after counting their reports.
    COUNT(e1.id) >= 5; -- Require at least five direct reports.
