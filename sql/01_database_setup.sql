-- ============================================================
-- SHOPSPHERE E-COMMERCE ANALYTICS
-- DATABASE TABLE SETUP
-- ============================================================


-- ============================================================
-- 1. CUSTOMERS TABLE
-- ============================================================

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    gender VARCHAR(20),
    date_of_birth DATE,
    city VARCHAR(100),
    state VARCHAR(100),
    pincode VARCHAR(20),
    signup_date DATE
);


-- ============================================================
-- 2. PRODUCTS TABLE
-- ============================================================

CREATE TABLE products (
    product_id VARCHAR(20) PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(100),
    subcategory VARCHAR(100),
    brand VARCHAR(100),
    selling_price NUMERIC(12,2),
    cost_price NUMERIC(12,2),
    stock_quantity INTEGER
);


-- ============================================================
-- 3. ORDERS TABLE
-- ============================================================

CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    customer_id VARCHAR(20),
    order_date DATE,
    order_status VARCHAR(50),
    sales_channel VARCHAR(50),

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


-- ============================================================
-- 4. ORDER ITEMS TABLE
-- ============================================================

CREATE TABLE order_items (
    order_id VARCHAR(20),
    product_id VARCHAR(20),
    quantity INTEGER,
    unit_price NUMERIC(12,2),
    discount_pct NUMERIC(5,2),
    gross_amount NUMERIC(12,2),
    discount_amount NUMERIC(12,2),
    net_amount NUMERIC(12,2),

    PRIMARY KEY (order_id, product_id),

    CONSTRAINT fk_order_items_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_order_items_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);


-- ============================================================
-- 5. PAYMENTS TABLE
-- ============================================================

CREATE TABLE payments (
    payment_id VARCHAR(20) PRIMARY KEY,
    order_id VARCHAR(20),
    payment_date DATE,
    payment_method VARCHAR(50),
    payment_status VARCHAR(50),
    payment_amount NUMERIC(12,2),

    CONSTRAINT fk_payments_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
);


-- ============================================================
-- DATABASE SETUP COMPLETE
-- ============================================================
SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'public'
ORDER BY table_name;