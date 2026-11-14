-- Task: Find authors who viewed their own articles, sorted by author ID.
SELECT DISTINCT author_id AS id -- Return each qualifying author only once.
FROM views -- Read all article viewing records.
WHERE -- Find views made by the article's own author.
    author_id = viewer_id -- Require author and viewer to be the same person.
ORDER BY -- Sort the resulting author IDs.
    id ASC; -- Put smaller IDs first.
