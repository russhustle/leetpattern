-- Task: Report each signed-up user's confirmed-request fraction, rounded
-- to two decimals; use zero for users with no confirmation requests.
SELECT -- Return every signed-up user and their confirmation rate.
    s.user_id, -- Identify the user.
    ROUND( -- Round the rate to two decimal places.
        -- Count confirmed requests and divide by all joined request rows.
        SUM(IF(c.action = 'confirmed', 1, 0)) / COUNT(*),
        2 -- Keep two digits after the decimal point.
    ) AS confirmation_rate -- Name the calculated fraction.
FROM signups AS s -- Include users even without confirmation requests.
-- No requests gives one NULL row, yielding 0/1 instead of division by zero.
LEFT JOIN confirmations AS c ON s.user_id = c.user_id
GROUP BY -- Calculate a separate rate for each user.
    s.user_id; -- Combine all of the user's requests.
