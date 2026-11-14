-- Task: Report the percentage of customers whose first order was immediate
-- (ordered for delivery that same day), rounded to two decimal places.
SELECT -- Calculate the requested percentage.
    -- Average 1/0 same-day delivery flags and convert to a rounded percentage.
    ROUND(100 * AVG(d.order_date = d.customer_pref_delivery_date), 2)
        AS immediate_percentage -- Name the requested percentage.
FROM Delivery AS d -- Read delivery orders.
WHERE (d.customer_id, d.order_date) IN ( -- Keep each customer's first order.
    SELECT -- Find the earliest order date per customer.
        f.customer_id, -- Identify the customer.
        MIN(f.order_date) AS first_order_date -- Choose their earliest order.
    FROM Delivery AS f -- Read all orders to determine first dates.
    GROUP BY f.customer_id -- Calculate one first-order date per customer.
); -- Match the selected first orders back to their delivery preferences.
