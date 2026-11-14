-- Task: Find customer names not referred by customer 2, including no referee.

-- 1. Handle a different referee and a missing referee separately.
SELECT NAME -- Return customer names.
FROM CUSTOMER -- Read all customers.
WHERE -- Exclude only customers referred by customer 2.
    REFEREE_ID <> 2 -- Include customers with another referee.
    OR REFEREE_ID IS NULL; -- Also include customers without a referee.

-- 2. Replace NULL with a value other than 2 for comparison.
SELECT NAME -- Return customer names.
FROM CUSTOMER -- Read all customers.
WHERE -- Keep customers without referee 2.
    COALESCE(REFEREE_ID, -1) <> 2; -- Treat a missing referee as -1.

-- 3. Equivalent COALESCE-based solution.
SELECT NAME -- Return customer names.
FROM CUSTOMER -- Read all customers.
WHERE -- Keep customers without referee 2.
    COALESCE(REFEREE_ID, -1) <> 2; -- Include NULL referees in the result.
