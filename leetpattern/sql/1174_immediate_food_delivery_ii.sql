SELECT
    ROUND(100 * AVG(d.order_date = d.customer_pref_delivery_date), 2)
        AS immediate_percentage
FROM Delivery AS d
WHERE (d.customer_id, d.order_date) IN (
    SELECT
        f.customer_id,
        MIN(f.order_date) AS first_order_date
    FROM Delivery AS f
    GROUP BY f.customer_id
);
