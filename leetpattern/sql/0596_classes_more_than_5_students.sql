-- Task: Report classes with at least five students.
SELECT class -- Return the qualifying class names.
FROM Courses -- Read student enrollments.
GROUP BY class -- Collect enrollments for each class.
HAVING COUNT(DISTINCT student) >= 5; -- Require at least five unique students.
