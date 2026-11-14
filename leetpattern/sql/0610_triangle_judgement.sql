-- Task: Report whether each set of three line segments can form a triangle.
SELECT -- Return the side lengths and their triangle classification.
    x, -- Keep the first side length.
    y, -- Keep the second side length.
    z, -- Keep the third side length.
    -- Every pair of sides must sum to more than the remaining side.
    CASE WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes' ELSE 'No' END
        AS triangle -- Name the Yes/No result.
FROM Triangle; -- Check every set of side lengths.
