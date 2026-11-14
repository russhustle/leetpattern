-- Task: Swap adjacent student pairs; leave a final unpaired seat unchanged.
-- Return the seating arrangement ordered by its new seat IDs.
SELECT -- Return each student with their reassigned seat.
    s.student, -- Keep the student's name.
    CASE -- Choose the new seat ID based on the original ID.
        WHEN MOD(s.id, 2) = 0 THEN s.id - 1 -- Move even seats one place back.
        WHEN -- Handle odd-numbered seats.
            -- Check that this is not the last seat.
            s.id < (SELECT MAX(last_seat.id) FROM Seat AS last_seat)
            THEN s.id + 1 -- Swap with the next, even-numbered seat.
        ELSE s.id -- Leave the last odd seat unchanged.
    END AS id -- Name the reassigned seat ID.
FROM Seat AS s -- Read the original seating arrangement.
ORDER BY id; -- Sort by the new seat IDs.
