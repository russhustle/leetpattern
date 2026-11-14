-- Task: For employees with direct reports, show their ID, name, report count,
-- and reports' average age rounded to an integer, ordered by employee ID.
SELECT -- Return manager details and direct-report statistics.
    m.employee_id, -- Identify the manager.
    m.name, -- Show the manager's name.
    COUNT(*) AS reports_count, -- Count employees reporting directly to them.
    ROUND(AVG(e.age)) AS average_age -- Round the reports' average age.
FROM Employees AS m -- Treat employees as potential managers.
-- Keep only managers with a matching direct report.
INNER JOIN Employees AS e ON m.employee_id = e.reports_to
GROUP BY m.employee_id, m.name -- Calculate statistics for each manager.
ORDER BY m.employee_id; -- Sort managers by employee ID ascending.
