-- Task: Report the user who rated the most movies and the highest-average-rated
-- movie in February 2020; break ties by the lexicographically smallest name.
( -- Find the user with the most ratings across all dates.
    SELECT u.name AS results -- Return the user's name in the shared column.
    -- Attach user names to their movie ratings.
    FROM MovieRating AS r INNER JOIN Users AS u ON r.user_id = u.user_id
    GROUP BY u.user_id, u.name -- Count ratings separately for each user.
    ORDER BY COUNT(*) DESC, u.name ASC -- Most ratings, then smallest name.
    LIMIT 1 -- Return only the winning user.
) -- Finish the user result.
UNION ALL -- Keep both results even if the user name and movie title match.
( -- Find the movie with the highest February average rating.
    SELECT m.title AS results -- Return the title in the same output column.
    -- Attach movie titles to their ratings.
    FROM MovieRating AS r INNER JOIN Movies AS m ON r.movie_id = m.movie_id
    -- Restrict ratings to February 2020.
    WHERE r.created_at >= '2020-02-01' AND r.created_at < '2020-03-01'
    GROUP BY m.movie_id, m.title -- Calculate each movie's February average.
    ORDER BY AVG(r.rating) DESC, m.title ASC -- Break equal averages by title.
    LIMIT 1 -- Return only the winning movie.
); -- Finish the combined two-row result.
