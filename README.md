# ShopSphere — E-Commerce Analytics

An end-to-end e-commerce analytics project built to analyze sales performance, customer behavior, product performance, and payment activity using Python, SQL, PostgreSQL, and Power BI.

---

## 📌 Project Overview

ShopSphere is a complete data analytics project that follows a real-world analytics workflow:

**Raw Data → Data Cleaning → Exploratory Data Analysis → SQL Analysis → Power BI Dashboard → Business Insights**

The project analyzes e-commerce transactions across customers, products, orders, order items, and payments to identify trends, customer segments, product performance, and business opportunities.

---

## 🎯 Business Objectives

The project answers key business questions such as:

- How much revenue is being generated?
- How are sales changing over time?
- Which product categories generate the most revenue?
- Which products are the top performers?
- How many new, returning, and VIP customers are there?
- Which customer segments contribute the most revenue?
- What is the average order value?
- Which payment methods are most commonly used?
- What proportion of payments are successful, pending, or failed?
- What business opportunities can be identified from the data?

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data generation, cleaning, validation and analysis |
| Pandas | Data manipulation and transformation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Exploratory data visualization |
| Jupyter Notebook | Analysis and documentation |
| PostgreSQL | Relational database and SQL analysis |
| SQL | Data quality checks and business analysis |
| Power BI | Interactive dashboards and business reporting |
| Git & GitHub | Version control and project management |

---

## 📊 Dataset

The project contains five main datasets:

| Dataset | Description |
|---|---|
| Customers | Customer demographic and registration information |
| Products | Product and category information |
| Orders | Order-level transaction information |
| Order Items | Individual products included in each order |
| Payments | Payment transactions and payment status |

---

## 🔄 Project Workflow

### 1. Data Generation

Synthetic e-commerce data was generated using Python.

### 2. Data Understanding

The datasets were explored to understand:

- Data types
- Dataset dimensions
- Missing values
- Duplicate records
- Unique values
- Relationships between tables

### 3. Data Cleaning

Python was used to:

- Handle missing values
- Standardize data types
- Validate records
- Clean categorical fields
- Prepare analysis-ready datasets

### 4. Exploratory Data Analysis

EDA was performed to analyze:

- Monthly revenue
- Monthly orders
- Customer trends
- Product performance
- Category performance
- Average order value
- Customer segmentation
- Brand and product performance

### 5. PostgreSQL & SQL Analysis

The cleaned datasets were loaded into PostgreSQL.

SQL was used for:

- Data quality validation
- Sales analysis
- Customer analysis
- Product analysis
- Payment analysis
- Business insights

### 6. Power BI Dashboard

The final analytics model was connected to Power BI to create interactive dashboards.

---

## 📈 Power BI Dashboard

The Power BI report contains five analytical pages:

### 1. Sales Analytics
Analyzes overall sales performance, revenue trends, orders, units sold, customer types, payment methods, and order status.

### 2. Customer Analytics
Analyzes customer segmentation, customer contribution to revenue, and top customers.

### 3. Product Analytics
Analyzes category performance, units sold, revenue, and top-performing products.

### 4. Payment Analytics
Analyzes payment methods, payment status, and revenue collection.

### 5. Business Insights
Summarizes key findings and translates the analysis into business recommendations.

---

## 💡 Key Business Insights

### Customer Retention
VIP and returning customers contribute a substantial portion of overall revenue, highlighting the importance of repeat purchases and customer retention.

### New Customer Opportunity
New customers contribute a relatively small share of revenue, creating an opportunity to improve customer conversion and retention.

### Category Performance
Electronics is the strongest-performing product category by revenue.

### Product Performance
Multiple products generate strong revenue, indicating that sales are not dependent on a single bestseller.

---

## 📌 Business Recommendations

- Strengthen loyalty programs for VIP and returning customers.
- Use targeted promotions to improve new-customer conversion.
- Maintain strong inventory availability for high-performing Electronics products.
- Use cross-selling and product bundles to increase average order value.
- Review pricing, promotions, and product assortment in lower-performing categories.

---

## 📁 Project Structure

```text
ShopSphere/
│
├── dashboard/
│   └── ShopSphere.pbix
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_eda.ipynb
│
├── sql/
│   ├── 01_database_setup.sql
│   ├── 02_data_quality.sql
│   ├── 03_sales_analysis.sql
│   ├── 04_customer_analysis.sql
│   ├── 05_product_analysis.sql
│   ├── 06_payment_analysis.sql
│   └── 07_business_insights.sql
│
├── src/
│   └── data_generation/
│
├── .gitignore
├── README.md
└── requirements.txt