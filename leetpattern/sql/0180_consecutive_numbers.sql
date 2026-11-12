SELECT DISTINCT a.num AS ConsecutiveNums
FROM Logs AS a
INNER JOIN Logs AS b ON b.id = a.id + 1 AND a.num = b.num
INNER JOIN Logs AS c ON c.id = a.id + 2 AND a.num = c.num;
