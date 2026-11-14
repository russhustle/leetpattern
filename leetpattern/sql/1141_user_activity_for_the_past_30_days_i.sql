-- Task: Count daily active users in the 30 days ending 2019-07-27 inclusive.
-- Return only days on which users were active.
SELECT -- Return each active date and its unique user count.
    activity_date AS day, -- Name the activity date as required.
    COUNT(DISTINCT user_id) AS active_users -- Count each user once per day.
FROM Activity -- Read all user activity records.
WHERE -- Restrict activity to the inclusive 30-day window.
    activity_date BETWEEN DATE_SUB( -- Calculate the beginning of the window.
        '2019-07-27', INTERVAL 29 DAY -- Subtract 29 days from the final day.
    ) AND '2019-07-27' -- Include the final day as well.
GROUP BY activity_date; -- Produce one count for each active day.
