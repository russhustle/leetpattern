-- Task: Delete duplicate emails, keeping the row with the smallest ID.
DELETE p1 -- Delete only the duplicate rows identified by p1.
FROM Person AS p1 -- Consider each person as a potential duplicate.
-- A matching email with a smaller ID means p1 must be removed.
INNER JOIN Person AS p2 ON p1.email = p2.email AND p1.id > p2.id;
