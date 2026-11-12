SELECT
    p.product_id,
    COALESCE(c.new_price, 10) AS price
FROM (SELECT DISTINCT product_id FROM Products) AS p
LEFT JOIN Products AS c
    ON
        p.product_id = c.product_id
        AND c.change_date = (
            SELECT MAX(history.change_date) FROM Products AS history
            WHERE
                history.product_id = p.product_id
                AND history.change_date <= '2019-08-16'
        );
