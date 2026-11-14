-- Task: Sum 2016 investment values for policies sharing a 2015 value with
-- another policy but having a unique location; round to two decimal places.
SELECT ROUND(SUM(i.tiv_2016), 2) AS tiv_2016 -- Sum qualifying 2016 values.
FROM Insurance AS i -- Evaluate every insurance policy.
WHERE i.tiv_2015 IN ( -- Require a 2015 value shared by multiple policies.
    SELECT v.tiv_2015 -- Return repeated 2015 values.
    FROM Insurance AS v -- Examine all policies for shared values.
    GROUP BY v.tiv_2015 -- Group policies with the same 2015 value.
    HAVING COUNT(*) > 1 -- Keep only values appearing more than once.
) -- Finish the shared-value filter.
AND (i.lat, i.lon) IN ( -- Also require a unique latitude/longitude pair.
    SELECT -- Return coordinates used by exactly one policy.
        loc.lat, -- Keep the latitude.
        loc.lon -- Keep the longitude.
    FROM Insurance AS loc -- Examine all policy locations.
    GROUP BY loc.lat, loc.lon -- Treat each coordinate pair as one location.
    HAVING COUNT(*) = 1 -- Exclude locations shared by multiple policies.
); -- Finish the unique-location filter.
