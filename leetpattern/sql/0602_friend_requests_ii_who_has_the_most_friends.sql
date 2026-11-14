-- Task: Find the person with the most friends and report their friend count.
SELECT -- Return the winning person and their number of friends.
    id, -- Identify the person.
    COUNT(*) AS num -- Count each accepted friendship involving this person.
FROM ( -- Collect both endpoints of every accepted friendship.
    SELECT requester_id AS id FROM RequestAccepted -- Include request senders.
    UNION ALL -- Keep every occurrence because each represents a friendship.
    SELECT accepter_id AS id FROM RequestAccepted -- Include request receivers.
) AS friends -- Treat both sets of people as one list.
GROUP BY id -- Count friendships for each person.
ORDER BY num DESC -- Place the person with the most friends first.
LIMIT 1; -- Return the single winner guaranteed by the problem.
