# SQL Beginner Challenge #13: Filtering NULL Values with IS NULL and IS NOT NULL

**Difficulty:** Beginner  
**Estimated time:** 10–15 minutes  
**Concepts:** `NULL`, `IS NULL`, `IS NOT NULL`, filtering data  

This challenge teaches how to correctly filter rows based on missing or present values in SQL—an essential skill for data quality checks and analysis.

---

## 🧠 The Problem

After reviewing product data, a data analyst asks:

> “Which products still have missing information?”

In SQL, `NULL` values require special handling.  
Standard comparison operators (`=` or `!=`) do **not** work with `NULL`.

Your task is to correctly identify rows with missing values.

---

## 📊 Table Schema

### `products`

| Column Name | Type | Description |
|------------|------|-------------|
| product_id | INTEGER | Unique product ID |
| name | TEXT | Product name |
| category | TEXT | Product category |
| supplier_notes | TEXT | Optional supplier notes (can be NULL) |

---

## 🧪 Sample Data

| product_id | name | category | supplier_notes |
|-----------:|------|----------|----------------|
| 101 | Wireless Mouse | Accessories | NULL |
| 102 | Mechanical Keyboard | Accessories | Best seller |
| 103 | 27-inch Monitor | Displays | NULL |
| 104 | USB-C Hub | Accessories | Limited stock |
| 105 | Laptop Stand | Workspace | NULL |

---

## ✅ Requirements

Your query must:

- Return:
  - `name`
  - `supplier_notes`
- Include **only rows where `supplier_notes` is missing**
- Use `IS NULL`
- Not use `= NULL`
- Not use `SELECT *`

---

## ✍️ Your Task

Write a SQL query that fulfills the requirements.

```sql
-- Write your query here


