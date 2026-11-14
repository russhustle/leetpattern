-- Task: Report employees whose bonus is below 1000 or who have no bonus record.

-- 1. Check low bonuses and missing bonuses explicitly.
SELECT -- Return employee names and their recorded bonuses.
    e.name, -- Show the employee's name.
    b.bonus -- Show the bonus, or NULL when no record exists.
FROM employee AS e -- Include employees even without bonus records.
LEFT JOIN bonus AS b ON e.empid = b.empid -- Attach any matching bonus.
WHERE -- Keep either a low bonus or a missing bonus.
    b.bonus < 1000 -- Include bonuses below the threshold.
    OR b.bonus IS NULL; -- Include employees without a recorded bonus.

-- 2. Treat a missing bonus as zero when filtering.
SELECT -- Return the same employee and bonus columns.
    e.name, -- Show the employee's name.
    b.bonus -- Preserve NULL in the output for missing bonuses.
FROM employee AS e -- Include employees with no bonus record.
LEFT JOIN bonus AS b ON e.empid = b.empid -- Attach any matching bonus.
WHERE -- Apply a single threshold check.
    COALESCE(b.bonus, 0) < 1000; -- Use zero only for the comparison.
