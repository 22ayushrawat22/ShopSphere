# ShopSphere — Data Dictionary

## 1. Customers

| Column | Data Type | Description | Key |
|---|---|---|---|
| customer_id | String | Unique customer identifier | Primary Key |
| first_name | String | Customer first name | |
| last_name | String | Customer last name | |
| gender | String | Customer gender | |
| date_of_birth | Date | Customer date of birth | |
| city | String | Customer city | |
| state | String | Customer state | |
| pincode | String | Customer postal code | |
| signup_date | Date | Date customer registered | |
| customer_type | String | Customer classification | |

---

## 2. Products

| Column | Data Type | Description | Key |
|---|---|---|---|
| product_id | String | Unique product identifier | Primary Key |
| product_name | String | Product name | |
| category | String | Main product category | |
| subcategory | String | Product subcategory | |
| brand | String | Product brand | |
| selling_price | Float | Current selling price | |
| cost_price | Float | Product acquisition cost | |
| stock_quantity | Integer | Current stock | |
| rating | Float | Average product rating | |
| launch_date | Date | Product launch date | |

---

## 3. Orders

| Column | Data Type | Description | Key |
|---|---|---|---|
| order_id | String | Unique order identifier | Primary Key |
| customer_id | String | Customer who placed order | Foreign Key |
| order_date | Date | Order placement date | |
| order_status | String | Current order status | |
| shipping_city | String | Delivery city | |
| payment_method | String | Payment method used | |
| coupon_code | String | Coupon applied | |
| discount_amount | Float | Order-level discount | |
| shipping_fee | Float | Shipping charge | |

---

## 4. Order Items

| Column | Data Type | Description | Key |
|---|---|---|---|
| order_item_id | String | Unique order-item identifier | Primary Key |
| order_id | String | Associated order | Foreign Key |
| product_id | String | Purchased product | Foreign Key |
| quantity | Integer | Number of units purchased | |
| unit_price | Float | Actual price per unit at purchase | |
| discount_amount | Float | Discount applied to item | |

---

## 5. Payments

| Column | Data Type | Description | Key |
|---|---|---|---|
| payment_id | String | Unique payment identifier | Primary Key |
| order_id | String | Associated order | Foreign Key |
| payment_date | Date | Payment date | |
| payment_method | String | Payment method | |
| payment_status | String | Payment status | |
| amount | Float | Payment amount | |

---

## 6. Reviews

| Column | Data Type | Description | Key |
|---|---|---|---|
| review_id | String | Unique review identifier | Primary Key |
| customer_id | String | Reviewing customer | Foreign Key |
| product_id | String | Reviewed product | Foreign Key |
| order_id | String | Associated order | Foreign Key |
| rating | Integer | Rating from 1 to 5 | |
| review_date | Date | Review date | |
| review_text | String | Customer review text | |

---

## 7. Returns

| Column | Data Type | Description | Key |
|---|---|---|---|
| return_id | String | Unique return identifier | Primary Key |
| order_id | String | Associated order | Foreign Key |
| order_item_id | String | Specific returned item | Foreign Key |
| customer_id | String | Customer requesting return | Foreign Key |
| return_date | Date | Return date | |
| return_reason | String | Reason for return | |
| refund_amount | Float | Refunded amount | |