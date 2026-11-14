-- Task: Report each project's average employee experience, rounded to two
-- decimal places.
SELECT -- Return each project and its average experience.
    p.project_id, -- Identify the project.
    ROUND(AVG(e.experience_years), 2) AS average_years -- Average experience.
FROM project AS p -- Read employee assignments for each project.
-- Attach each assigned employee's years of experience.
LEFT JOIN employee AS e ON p.employee_id = e.employee_id
GROUP BY -- Calculate an independent average for each project.
    p.project_id -- Combine assignments belonging to the same project.
