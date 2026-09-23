-- ============================================================
-- SHOPSPHERE - SALES ANALYSIS
-- ============================================================


-- 1. TOTAL ORDERS
SELECT COUNT(*) AS total_orders
FROM orders;


-- 2. TOTAL UNITS SOLD
SELECT SUM(quantity) AS total_units_sold
FROM order_items;


-- 3. TOTAL REVENUE
SELECT
    SUM(quantity * unit_price * (1 - discount_pct / 100.0))
    AS total_revenue
FROM order_items;


-- 4. TOTAL GROSS SALES
SELECT
    SUM(quantity * unit_price)
    AS gross_sales
FROM order_items;


-- 5. TOTAL DISCOUNT
SELECT
    SUM(quantity * unit_price * discount_pct / 100.0)
    AS total_discount
FROM order_items;


-- 6. AVERAGE ORDER VALUE
SELECT
    SUM(oi.quantity * oi.unit_price * (1 - oi.discount_pct / 100.0))
    / COUNT(DISTINCT oi.order_id)
    AS average_order_value
FROM order_items oi;


-- 7. MONTHLY REVENUE
SELECT
    DATE_TRUNC('month', o.order_date) AS month,
    SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_pct / 100.0)
    ) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY DATE_TRUNC('month', o.order_date)
ORDER BY month;


-- 8. REVENUE BY ORDER STATUS
SELECT
    o.order_status,
    SUM(
        oi.quantity * oi.unit_price *
        (1 - oi.discount_pct / 100.0)
    ) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY o.order_status
ORDER BY revenue DESC;