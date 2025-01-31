-- Find all tweets that have a content length greater than 15 characters
SELECT tweet_id
FROM
    tweets
WHERE
    LENGTH(content) > 15
