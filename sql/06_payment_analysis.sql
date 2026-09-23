-- ============================================================
-- SHOPSPHERE - PAYMENT ANALYSIS
-- ============================================================

-- 1. Payment methods
SELECT
    payment_method,
    COUNT(*) AS total_payments,
    ROUND(SUM(payment_amount), 2) AS total_amount
FROM payments
GROUP BY payment_method
ORDER BY total_amount DESC;


-- 2. Payment status
SELECT
    payment_status,
    COUNT(*) AS total_payments,
    ROUND(SUM(payment_amount), 2) AS total_amount
FROM payments
GROUP BY payment_status
ORDER BY total_payments DESC;


-- 3. Successful payment revenue
SELECT
    ROUND(SUM(payment_amount), 2) AS successful_payment_revenue
FROM payments
WHERE payment_status = 'Completed';


-- 4. Failed payments
SELECT
    COUNT(*) AS failed_payments
FROM payments
WHERE payment_status = 'Failed';


-- 5. Payment method success
SELECT
    payment_method,
    COUNT(*) AS total_transactions,
    COUNT(*) FILTER (
        WHERE payment_status = 'Completed'
    ) AS successful_transactions,
    ROUND(
        COUNT(*) FILTER (
            WHERE payment_status = 'Completed'
        ) * 100.0 / COUNT(*),
        2
    ) AS success_rate_percentage
FROM payments
GROUP BY payment_method
ORDER BY success_rate_percentage DESC;


-- 6. Average payment amount
SELECT
    ROUND(AVG(payment_amount), 2) AS average_payment_amount
FROM payments;


-- 7. Largest payments
SELECT
    payment_id,
    order_id,
    payment_method,
    payment_status,
    payment_amount
FROM payments
ORDER BY payment_amount DESC
LIMIT 10;

-- Convert refunded payment status to pending
UPDATE public.payments
SET payment_status = 'Pending'
WHERE payment_status = 'Refunded';

-- Verify payment status distribution
SELECT payment_status, COUNT(*) AS payment_count
FROM public.payments
GROUP BY payment_status
ORDER BY payment_count DESC;