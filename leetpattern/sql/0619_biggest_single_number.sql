-- Task: Find the largest number appearing exactly once, or NULL if none exists.
SELECT MAX(num) AS num -- Return the largest unique number, or NULL.
FROM ( -- First collect numbers that appear only once.
    SELECT num FROM MyNumbers -- Read the input numbers.
    GROUP BY num -- Count occurrences of each number.
    HAVING COUNT(*) = 1 -- Keep numbers with exactly one occurrence.
) AS singles; -- Use the unique numbers as input to MAX.
