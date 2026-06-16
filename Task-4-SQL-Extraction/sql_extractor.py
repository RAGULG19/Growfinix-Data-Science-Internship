import sqlite3
import pandas as pd

# 1. Create a Local Mock SQLite Database & Connection
conn = sqlite3.connect('growfinix_orders.db')
cursor = conn.cursor()

# 2. Create a Sample Orders Table (Backend Mock Setup)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        customer_name TEXT,
        product_category TEXT,
        order_amount REAL,
        order_date TEXT
    )
''')

# 3. Insert Dummy Data into the SQL Database Table
sample_data = [
    (101, 'Rahul', 'Electronics', 45000.00, '2026-06-10'),
    (102, 'Priya', 'Fashion', 3500.50, '2026-06-12'),
    (103, 'Vijay', 'Electronics', 12000.00, '2026-06-14'),
    (104, 'Ananya', 'Home Decor', 8500.00, '2026-06-15'),
    (105, 'Deepak', 'Fashion', 2400.00, '2026-06-16')
]

cursor.executemany('''
    INSERT OR IGNORE INTO orders (order_id, customer_name, product_category, order_amount, order_date)
    VALUES (?, ?, ?, ?, ?)
''', sample_data)
conn.commit()

# 4. Core Task Requirement: Execute SQL Query to Extract Data
# Filtering high-value orders or group analysis
sql_query = "SELECT * FROM orders WHERE order_amount > 5000"

# 5. Extract Unstructured SQL Rows into a Structured Pandas DataFrame
df_extracted = pd.read_sql_query(sql_query, conn)

# Close Database connection
conn.close()

# 6. Display Output Terminal Log
print("--- SUCCESS: EXTRACTED HIGH-VALUE ORDERS VIA SQL ---")
print(df_extracted)