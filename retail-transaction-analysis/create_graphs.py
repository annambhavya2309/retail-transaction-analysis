
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the existing database
conn = sqlite3.connect("retail_store.db")

# Load cleaned data
df = pd.read_csv("cleaned_transactions.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# 1. Daily sales trend
daily_sales = df.groupby(df["timestamp"].dt.date)["price"].sum()

plt.figure(figsize=(8, 5))
daily_sales.plot(kind="line", marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("daily_sales_trend.png")
plt.show()

# 2. Sales by product category
category_sales = df.groupby("item_category")["price"].sum().sort_values(ascending=False)

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Product Category")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("category_sales.png")
plt.show()

# 3. Payment method comparison
payment_data = pd.read_sql_query("""
    SELECT payment_method,
           COUNT(receipt_id) AS total_transactions,
           ROUND(SUM(price), 2) AS total_sales
    FROM transactions
    GROUP BY payment_method
""", conn)

plt.figure(figsize=(7, 5))
plt.bar(payment_data["payment_method"], payment_data["total_transactions"])
plt.title("Transactions by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Number of Transactions")
plt.tight_layout()
plt.savefig("payment_method_analysis.png")
plt.show()

conn.close()

print("All three graphs created successfully!")
