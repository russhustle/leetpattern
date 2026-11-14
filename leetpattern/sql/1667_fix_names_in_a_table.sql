-- Task: Capitalize the first letter of each user's name, lowercase the rest,
-- and return users ordered by ID.
SELECT -- Return each user with their normalized name.
    user_id, -- Preserve the user's ID.
    -- Uppercase the first character and append the lowercase remainder.
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM Users -- Read the original user names.
ORDER BY user_id; -- Sort results by user ID ascending.
