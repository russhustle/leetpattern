-- Task: Find non-boring movies with odd IDs, ordered by rating descending.
SELECT -- Return all requested movie details.
    id, -- Show the movie's ID.
    movie, -- Show the movie's title.
    description, -- Show its description.
    rating -- Show its rating.
FROM Cinema -- Read the movie catalog.
WHERE -- Apply both eligibility conditions.
    MOD(id, 2) = 1 -- Keep only odd-numbered IDs.
    AND description <> 'boring' -- Exclude movies described as boring.
ORDER BY rating DESC; -- List the highest-rated movies first.
