SELECT
    id,
    movie,
    description,
    rating
FROM
    cinema
WHERE
    id % 2 = 1
    AND LOWER(description) NOT LIKE '%boring%'
ORDER BY
    rating DESC;
