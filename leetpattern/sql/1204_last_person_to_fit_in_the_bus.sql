-- Task: Find the last person who can board without exceeding the bus's
-- 1000-kilogram capacity, following queue order.
WITH boarding AS ( -- Calculate the cumulative weight as people board.
    SELECT -- Keep each person, their turn, and the total weight at that turn.
        person_name, -- Identify the passenger by name.
        turn, -- Keep the passenger's boarding order.
        -- Add each passenger's weight to the weights of earlier passengers.
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue -- Read the ordered boarding queue.
) -- Finish the cumulative-weight result.

SELECT person_name -- Return the last eligible passenger's name.
FROM boarding -- Use the calculated cumulative weights.
WHERE total_weight <= 1000 -- Keep turns that do not exceed capacity.
ORDER BY turn DESC -- Put the latest eligible boarding turn first.
LIMIT 1; -- Return only that passenger.
