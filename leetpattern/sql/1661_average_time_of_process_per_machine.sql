-- Task: Report each machine's average process duration, rounded to three
-- decimal places, using the difference between each process's end and start.
SELECT -- Return machine IDs and average processing times.
    a1.machine_id, -- Identify the machine.
    -- Average end-minus-start durations, then round to three decimals.
    ROUND(AVG(a2.timestamp - a1.timestamp), 3) AS processing_time
    -- Equivalent calculation using total duration divided by process count:
    -- ROUND(SUM(a2.timestamp - a1.timestamp) / COUNT(*), 3) AS processing_time
FROM activity AS a1 -- Represent process starts in the matched pairs.
INNER JOIN activity AS a2 -- Match each start with its corresponding end.
    ON -- Pair records belonging to the same machine and process.
        a1.machine_id = a2.machine_id -- Require the same machine.
        AND a1.process_id = a2.process_id -- Require the same process.
        -- Each process has one start and one end; choose the earlier first.
        AND a1.timestamp < a2.timestamp
GROUP BY -- Average all matched process durations per machine.
    a1.machine_id; -- Produce one result per machine.
