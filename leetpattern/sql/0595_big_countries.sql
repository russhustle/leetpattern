-- Task: Report countries with at least 25 million people or 3 million km².
SELECT -- Return the requested country details.
    NAME, -- Show the country's name.
    POPULATION, -- Show its population.
    AREA -- Show its area in square kilometers.
FROM WORLD -- Read country information.
WHERE -- Either size criterion is sufficient.
    POPULATION >= 25000000 -- Include populations of at least 25 million.
    OR AREA >= 3000000; -- Include areas of at least 3 million km².
