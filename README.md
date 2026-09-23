# ShopSphere — E-Commerce Analytics

An end-to-end e-commerce analytics project that transforms raw transactional data into actionable business insights using Python, PostgreSQL, SQL, and Power BI.

---

## 📌 Project Overview

ShopSphere is an end-to-end data analytics project designed to analyze e-commerce sales, customer behavior, product performance, and payment activity.

The project follows a complete analytics workflow:

**Raw Data → Data Cleaning → Exploratory Data Analysis → PostgreSQL → SQL Analysis → Power BI → Business Insights**

The objective is to simulate a real-world analytics environment where data is cleaned, validated, analyzed, visualized, and converted into business recommendations.

---

## 🎯 Business Objectives

The project focuses on answering important business questions such as:

- How much revenue is the business generating?
- How many orders and customers does the platform have?
- Which product categories generate the most revenue?
- Which products are the top performers?
- How do new, returning, and VIP customers contribute to revenue?
- What is the average order value?
- Which payment methods are most frequently used?
- What is the distribution of successful, pending, and failed payments?
- Where are the major opportunities for customer retention and revenue growth?

---

## 🗂️ Dataset

The project uses five main datasets:

| Dataset | Description |
|---|---|
| Customers | Customer demographic and registration information |
| Products | Product and category information |
| Orders | Order-level transaction information |
| Order Items | Individual products included in each order |
| Payments | Payment transactions and payment status |

The cleaned datasets are stored in:

```text
data/processed/