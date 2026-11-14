-- Task: Find numbers appearing at least three times consecutively in Logs.
SELECT DISTINCT a.num AS ConsecutiveNums -- Return each qualifying number once.
FROM Logs AS a -- Treat each log entry as the start of a possible sequence.
-- Match the next ID and require the same number.
INNER JOIN Logs AS b ON b.id = a.id + 1 AND a.num = b.num
-- Match the following ID and require the same number again.
INNER JOIN Logs AS c ON c.id = a.id + 2 AND a.num = c.num;
