-- Task: Find employees earning below 30000 whose assigned manager no longer
-- exists in Employees; return employee IDs in ascending order.
SELECT e.employee_id -- Return the qualifying employee IDs.
FROM Employees AS e -- Examine each current employee.
-- Look up the assigned manager while keeping employees with missing managers.
LEFT JOIN Employees AS m ON e.manager_id = m.employee_id
-- Require low salary, an assigned manager ID, and no matching manager record.
WHERE e.salary < 30000 AND e.manager_id IS NOT NULL AND m.employee_id IS NULL
ORDER BY e.employee_id; -- Sort the resulting employee IDs ascending.
