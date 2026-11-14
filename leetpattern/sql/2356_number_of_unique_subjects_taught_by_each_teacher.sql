-- Task: Count each teacher's distinct subjects across all departments.
SELECT -- Return each teacher and their unique subject count.
    teacher_id, -- Identify the teacher.
    COUNT(DISTINCT subject_id) AS cnt -- Count each subject once per teacher.
FROM Teacher -- Read teaching assignments.
GROUP BY teacher_id; -- Combine all assignments for the same teacher.
