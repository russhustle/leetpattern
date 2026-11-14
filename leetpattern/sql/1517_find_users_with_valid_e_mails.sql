-- Task: Find users whose email starts with a letter, has only letters, digits,
-- underscores, periods, or hyphens before @, and ends with @leetcode.com.
SELECT -- Return the details of users with valid email addresses.
    user_id, -- Identify the user.
    name, -- Show the user's name.
    mail -- Show the email address that passed validation.
FROM Users -- Read registered users.
-- Anchor the entire address; 'c' makes the domain check case-sensitive.
WHERE REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$', 'c');
