-- Task: Report the percentage of all users registered for each contest,
-- rounded to two decimals, sorted by percentage descending then contest ID.
SELECT -- Return contest IDs and their registration percentages.
    r.contest_id, -- Identify the contest.
    ROUND( -- Round the calculated percentage to two decimal places.
        -- Divide unique registrants by all users and convert to a percentage.
        COUNT(DISTINCT r.user_id) * 100.0 / (SELECT COUNT(*) FROM users),
        2 -- Keep two digits after the decimal point.
    ) AS percentage -- Name the registration percentage.
FROM register AS r -- Read users' contest registrations.
GROUP BY -- Calculate a separate percentage per contest.
    r.contest_id -- Combine registrations for the same contest.
ORDER BY -- Apply the required ranking and tie-breaker.
    percentage DESC, -- Put the highest registration percentage first.
    contest_id ASC -- Break percentage ties using the smaller contest ID.
