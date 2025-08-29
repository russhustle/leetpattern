SELECT tweet_id
FROM
    tweets
WHERE
    CHAR_LENGTH(content) > 15;
