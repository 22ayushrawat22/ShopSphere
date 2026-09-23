-- SHOPSPHERE DATA QUALITY CHECKS

-- 1. Row counts
SELECT 'customers' AS table_name, COUNT(*) AS row_count FROM public.customers
UNION ALL
SELECT 'products', COUNT(*) FROM public.products
UNION ALL
SELECT 'orders', COUNT(*) FROM public.orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM public.order_items
UNION ALL
SELECT 'payments', COUNT(*) FROM public.payments;


-- 2. Missing customer IDs
SELECT COUNT(*) AS missing_customer_ids
FROM public.customers
WHERE customer_id IS NULL;


-- 3. Duplicate customer IDs
SELECT customer_id, COUNT(*) AS duplicate_count
FROM public.customers
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- 4. Duplicate product IDs
SELECT product_id, COUNT(*) AS duplicate_count
FROM public.products
GROUP BY product_id
HAVING COUNT(*) > 1;


-- 5. Invalid product prices
SELECT COUNT(*) AS invalid_prices
FROM public.products
WHERE selling_price < 0
   OR cost_price < 0;


-- 6. Invalid stock
SELECT COUNT(*) AS invalid_stock
FROM public.products
WHERE stock_quantity < 0;


-- 7. Invalid order quantities
SELECT COUNT(*) AS invalid_quantities
FROM public.order_items
WHERE quantity <= 0;


-- 8. Invalid discounts
SELECT COUNT(*) AS invalid_discounts
FROM public.order_items
WHERE discount_pct < 0
   OR discount_pct > 100;