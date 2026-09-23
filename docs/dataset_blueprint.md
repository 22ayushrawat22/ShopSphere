# ShopSphere — Dataset Blueprint

## 1. Project Dataset Overview

ShopSphere will contain seven interconnected datasets representing an Indian e-commerce business.

| Table | Target Records |
|---|---:|
| Customers | 20,000 |
| Products | 1,000 |
| Orders | 100,000 |
| Order Items | ~200,000 |
| Payments | ~100,000 |
| Reviews | ~60,000 |
| Returns | ~15,000 |

Data period: 01 January 2024 to 31 December 2025.

---

## 2. Customers

Target: 20,000

Primary Key: customer_id

Customer IDs:

C00001–C20000

Customer behavior will include one-time, occasional, regular and loyal purchasing patterns.

Customers will be distributed across approximately 30 Indian cities.

A customer cannot place an order before their signup date.

---

## 3. Products

Target: 1,000

Primary Key: product_id

Categories:

- Electronics
- Fashion
- Home & Kitchen
- Beauty & Personal Care
- Sports & Fitness
- Books

Each product contains a selling price and cost price.

cost_price < selling_price

Product quality will influence ratings and return probability.

---

## 4. Orders

Target: 100,000

Primary Key: order_id

Foreign Key: customer_id

Order dates must fall between 2024-01-01 and 2025-12-31.

A customer cannot order before signup.

Order statuses:

- Delivered
- Shipped
- Processing
- Cancelled
- Returned

---

## 5. Order Items

Target: approximately 200,000

Primary Key: order_item_id

Foreign Keys:

- order_id
- product_id

Each order can contain multiple products.

unit_price represents the actual transaction price at purchase time and must be used for historical revenue calculations.

---

## 6. Payments

Target: approximately 100,000

Primary Key: payment_id

Foreign Key: order_id

Payment methods:

- UPI
- Credit Card
- Debit Card
- Net Banking
- Wallet
- COD

Payment date cannot occur before order date.

---

## 7. Reviews

Target: approximately 60,000

Primary Key: review_id

Foreign Keys:

- customer_id
- product_id
- order_id

Ratings must normally be between 1 and 5.

A customer can review a product only if the customer purchased that product.

Review date cannot occur before order date.

---

## 8. Returns

Target: approximately 15,000

Primary Key: return_id

Foreign Keys:

- order_id
- order_item_id
- customer_id

Return reasons:

- Damaged
- Wrong Product
- Size Issue
- Quality Issue
- Changed Mind
- Late Delivery
- Other

A return must reference an existing order item.

Return date must occur after the original purchase.

---

## 9. Geographic Rules

Cities must map consistently to their respective Indian states.

Example:

Mumbai → Maharashtra
Pune → Maharashtra
Jaipur → Rajasthan
Bengaluru → Karnataka
Delhi → Delhi

---

## 10. Business Behavior

The dataset will contain realistic relationships between:

- customer behavior
- purchase frequency
- discounts
- revenue
- profit
- ratings
- returns
- seasonality

These relationships will be generated probabilistically rather than assigning fixed outcomes.

---

## 11. Seasonal Behavior

Higher activity will generally occur during:

- Republic Day Sale
- Summer Sale
- Independence Day Sale
- Festive Sale
- Diwali Sale
- Big Shopping Week
- Year End Sale

October–December will generally have stronger demand than several other periods.

---

## 12. Data Quality Problems

The raw dataset will intentionally contain approximately 1–3% controlled data-quality issues.

Examples:

- Missing values
- Duplicate records
- Leading/trailing spaces
- Inconsistent capitalization
- Inconsistent payment-method labels
- Multiple date formats
- Invalid ratings
- Invalid quantities
- Invalid discount values

Raw data will remain available and will never be overwritten.

---

## 13. Referential Integrity

The following relationships must remain valid:

customers.customer_id → orders.customer_id

orders.order_id → order_items.order_id

products.product_id → order_items.product_id

orders.order_id → payments.order_id

orders.order_id → reviews.order_id

customers.customer_id → reviews.customer_id

products.product_id → reviews.product_id

order_items.order_item_id → returns.order_item_id

orders.order_id → returns.order_id

customers.customer_id → returns.customer_id

---

## 14. Temporal Integrity

The following rules must hold:

signup_date <= order_date

order_date <= payment_date

order_date <= review_date

order_date < return_date

product launch_date <= purchase date

---

## 15. Financial Logic

Item Gross Value:

quantity × unit_price

Item Net Value:

(quantity × unit_price) - item_discount

Revenue and profit calculations will be formally defined before analysis to prevent double-counting discounts.

Historical transaction calculations must use the transaction-time unit_price rather than the current product selling_price.

---

## 16. Important Principle

The dataset should simulate realistic business behavior rather than simply contain random values.

The final business insights must be discovered through analysis rather than predetermined in advance.