-- ============================================================
-- SHOPSPHERE - FINAL BUSINESS INSIGHTS
-- ============================================================


-- 1. Overall Business KPIs
SELECT
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(DISTINCT o.customer_id) AS customers_with_orders,
    SUM(oi.quantity) AS total_units_sold,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ), 2
    ) AS total_revenue,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ) / COUNT(DISTINCT o.order_id),
        2
    ) AS average_order_value
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id;


-- 2. Monthly Sales Trend
SELECT
    DATE_TRUNC('month', o.order_date)::date AS month,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ), 2
    ) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY DATE_TRUNC('month', o.order_date)
ORDER BY month;


-- 3. Top 10 Customers
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    c.customer_type,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ), 2
    ) AS total_spent
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.customer_type
ORDER BY total_spent DESC
LIMIT 10;


-- 4. Top 10 Products
SELECT
    p.product_id,
    p.product_name,
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ), 2
    ) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY
    p.product_id,
    p.product_name,
    p.category
ORDER BY revenue DESC
LIMIT 10;


-- 5. Revenue by Category
SELECT
    p.category,
    SUM(oi.quantity) AS units_sold,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ), 2
    ) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY revenue DESC;


-- 6. Order Status Performance
SELECT
    o.order_status,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ), 2
    ) AS revenue
FROM orders o
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY o.order_status
ORDER BY total_orders DESC;


-- 7. Low Stock Products
SELECT
    product_id,
    product_name,
    category,
    stock_quantity
FROM products
WHERE stock_quantity < 50
ORDER BY stock_quantity ASC;


-- 8. Customer Type Performance
SELECT
    c.customer_type,
    COUNT(DISTINCT c.customer_id) AS customers,
    COUNT(DISTINCT o.order_id) AS orders,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ), 2
    ) AS revenue
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_type
ORDER BY revenue DESC;