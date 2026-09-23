-- ============================================================
-- SHOPSPHERE - CUSTOMER ANALYSIS
-- ============================================================

-- 1. Total customers by customer type
SELECT
    customer_type,
    COUNT(*) AS total_customers
FROM customers
GROUP BY customer_type
ORDER BY total_customers DESC;


-- 2. Customers by city
SELECT
    city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY city
ORDER BY total_customers DESC
LIMIT 10;


-- 3. Customers by state
SELECT
    state,
    COUNT(*) AS total_customers
FROM customers
GROUP BY state
ORDER BY total_customers DESC;


-- 4. Orders per customer
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_orders DESC
LIMIT 10;


-- 5. Top customers by spending
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_pct / 100.0)
    ) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC
LIMIT 10;


-- 6. Revenue by customer type
SELECT
    c.customer_type,
    SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_pct / 100.0)
    ) AS total_revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_type
ORDER BY total_revenue DESC;


-- 7. Average spending per customer
SELECT
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ) / COUNT(DISTINCT c.customer_id),
        2
    ) AS average_customer_spending
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id;