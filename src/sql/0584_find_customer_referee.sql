-- 1.
SELECT NAME
FROM
    CUSTOMER
WHERE
    REFEREE_ID <> 2
    OR REFEREE_ID IS NULL;

-- 2.
SELECT NAME
FROM
    CUSTOMER
WHERE
    COALESCE(REFEREE_ID, -1) <> 2;

-- 3.
SELECT NAME
FROM
    CUSTOMER
WHERE
    COALESCE(REFEREE_ID, -1) <> 2;
