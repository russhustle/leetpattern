SELECT ROUND(SUM(i.tiv_2016), 2) AS tiv_2016
FROM Insurance AS i
WHERE i.tiv_2015 IN (
    SELECT v.tiv_2015
    FROM Insurance AS v
    GROUP BY v.tiv_2015
    HAVING COUNT(*) > 1
)
AND (i.lat, i.lon) IN (
    SELECT
        loc.lat,
        loc.lon
    FROM Insurance AS loc
    GROUP BY loc.lat, loc.lon
    HAVING COUNT(*) = 1
);
