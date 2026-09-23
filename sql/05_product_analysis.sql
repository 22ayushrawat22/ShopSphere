-- ============================================================
-- SHOPSPHERE - PRODUCT ANALYSIS
-- ============================================================

-- 1. Products by category
SELECT
    category,
    COUNT(*) AS total_products
FROM products
GROUP BY category
ORDER BY total_products DESC;


-- 2. Revenue by category
SELECT
    p.category,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ), 2
    ) AS total_revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;


-- 3. Top 10 products by units sold
SELECT
    p.product_id,
    p.product_name,
    SUM(oi.quantity) AS units_sold
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY units_sold DESC
LIMIT 10;


-- 4. Top 10 products by revenue
SELECT
    p.product_id,
    p.product_name,
    ROUND(
        SUM(
            oi.quantity * oi.unit_price *
            (1 - oi.discount_pct / 100.0)
        ), 2
    ) AS revenue
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY revenue DESC
LIMIT 10;


-- 5. Product profit
SELECT
    p.product_id,
    p.product_name,
    ROUND(
        SUM(
            oi.quantity *
            (p.selling_price - p.cost_price)
        ), 2
    ) AS estimated_profit
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY estimated_profit DESC
LIMIT 10;


-- 6. Profit margin by category
SELECT
    p.category,
    ROUND(
        (
            SUM(
                oi.quantity *
                (p.selling_price - p.cost_price)
            )
            /
            NULLIF(
                SUM(oi.quantity * p.selling_price),
                0
            )
        ) * 100,
        2
    ) AS profit_margin_percentage
FROM products p
JOIN order_items oi
    ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY profit_margin_percentage DESC;


-- 7. Products with low stock
SELECT
    product_id,
    product_name,
    stock_quantity
FROM products
WHERE stock_quantity < 50
ORDER BY stock_quantity ASC;


-- 8. Products that have never been ordered
SELECT
    p.product_id,
    p.product_name,
    p.category
FROM products p
LEFT JOIN order_items oi
    ON p.product_id = oi.product_id
WHERE oi.product_id IS NULL;