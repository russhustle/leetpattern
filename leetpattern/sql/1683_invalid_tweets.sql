-- Task: Find tweet IDs whose content exceeds the 15-character limit.
SELECT tweet_id -- Return only invalid tweet IDs.
FROM tweets -- Read all stored tweets.
WHERE -- Check the character count rather than the byte count.
    CHAR_LENGTH(content) > 15; -- Keep tweets longer than 15 characters.
