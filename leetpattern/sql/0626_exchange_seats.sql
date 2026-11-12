SELECT
    s.student,
    CASE
        WHEN MOD(s.id, 2) = 0 THEN s.id - 1
        WHEN
            s.id < (SELECT MAX(last_seat.id) FROM Seat AS last_seat)
            THEN s.id + 1
        ELSE s.id
    END AS id
FROM Seat AS s
ORDER BY id;
