-- Task: Count each student's exam attendances for every subject, including
-- zero counts, ordered by student ID and subject name.
SELECT -- Return each student-subject pair and its attendance count.
    st.student_id, -- Identify the student.
    st.student_name, -- Show the student's name.
    su.subject_name, -- Identify the subject.
    COUNT(ex.student_id) AS attended_exams -- Count matches, ignoring NULL rows.
FROM students AS st -- Include all students, even those with no exams.
CROSS JOIN subjects AS su -- Generate every possible student-subject pair.
LEFT JOIN examinations AS ex -- Attach attendance while keeping missing exams.
    ON -- Match attendance for this student and this subject.
        st.student_id = ex.student_id -- Require the same student.
        AND su.subject_name = ex.subject_name -- Require the same subject.
GROUP BY -- Count exams separately for every student-subject pair.
    st.student_id, -- Group by the student's identity.
    st.student_name, -- Keep the student's name in the output.
    su.subject_name -- Separate each subject's attendance count.
ORDER BY -- Apply the required output order.
    st.student_id, -- Sort students by ID first.
    su.subject_name; -- Sort each student's subjects alphabetically.
