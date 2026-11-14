-- Task: Find the fraction of players returning the day after their first login.
-- Round the fraction to two decimal places.
SELECT -- Calculate the requested fraction.
    -- Divide returning players by all players and round to two decimals.
    ROUND(COUNT(DISTINCT a.player_id) / COUNT(DISTINCT f.player_id), 2)
        AS fraction -- Name the rounded result.
FROM -- First determine each player's initial login date.
    (SELECT -- Build one row per player.
        player_id, -- Identify the player.
        MIN(event_date) AS first_date -- Find their earliest login.
    FROM Activity -- Read login activity.
    GROUP BY player_id) AS f -- Collapse activity to each player's first date.
LEFT JOIN Activity AS a -- Keep all players, including those who never returned.
    ON -- Match activity to the same player on the next day.
        f.player_id = a.player_id -- Require the same player.
        -- Only a login exactly one day after the first counts as a return.
        AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY);
