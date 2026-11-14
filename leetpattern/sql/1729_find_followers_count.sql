-- Task: Report each user's follower count, ordered by user ID ascending.
SELECT -- Return each user and their number of followers.
    user_id, -- Identify the user being followed.
    COUNT(DISTINCT follower_id) AS followers_count -- Count unique followers.
FROM Followers -- Read the follower relationships.
GROUP BY user_id -- Collect all followers of the same user.
ORDER BY user_id ASC; -- List users from smallest to largest ID.
