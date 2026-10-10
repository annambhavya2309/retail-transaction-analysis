import sqlite3

def build_database():
    # Connect to SQLite database file
    conn = sqlite3.connect('retail_store.db')
    cursor = conn.cursor()

    # Create the transactions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        receipt_id INTEGER PRIMARY KEY,
        store_location TEXT,
        item_category TEXT,
        price REAL,
        payment_method TEXT,
        timestamp TEXT
    )
    ''')

    
    mock_data = [
    (101, 'Visakhapatnam', 'Electronics', 1200.00, 'Card', '2026-03-01 10:15:00'),
    (102, 'Vijayawada', 'Clothing', 45.50, 'Cash', '2026-03-01 11:30:00'),
    (103, 'Visakhapatnam', 'Home Decor', 89.99, 'Card', '2026-03-01 12:00:00'),
    (104, 'Vizianagaram', 'Electronics', 150.00, 'Card', '2026-03-02 09:45:00'),
    (105, 'Vijayawada', 'Groceries', 120.25, 'Cash', '2026-03-02 14:20:00'),
    (106, 'Visakhapatnam', 'Clothing', 65.00, 'Card', '2026-03-02 16:10:00'),
    (107, 'Vizianagaram', 'Home Decor', 210.00, 'Card', '2026-03-03 11:05:00'),
    (108, 'Vijayawada', 'Electronics', 85.00, 'Card', '2026-03-03 13:55:00'),
    (109, 'Visakhapatnam', 'Groceries', 34.10, 'Cash', '2026-03-03 17:30:00'),
    (110, 'Vizianagaram', 'Clothing', 110.00, 'Card', '2026-03-04 10:00:00'),
    (111, 'Visakhapatnam', 'Electronics', 1200.00, 'Card', '2026-03-01 10:15:00'),  # System duplicate record
    (112, 'Vijayawada', 'Home Decor', 315.50, 'Card', '2026-03-04 15:40:00'),
    (113, 'Vizianagaram', 'Groceries', 55.00, 'Cash', '2026-03-04 18:25:00'),
    (114, 'Visakhapatnam', 'Clothing', 78.25, 'Card', '2026-03-05 09:15:00'),
    (115, 'Vijayawada', 'Electronics', 450.00, 'Card', '2026-03-05 12:35:00'),
    (116, 'Vizianagaram', 'Home Decor', 42.00, 'Cash', '2026-03-05 14:50:00'),
    (117, 'Visakhapatnam', 'Groceries', 95.40, 'Card', '2026-03-06 11:20:00'),
    (118, 'Vijayawada', 'Clothing', 125.00, 'Card', '2026-03-06 16:05:00'),
    (119, 'Vizianagaram', 'Electronics', 230.00, 'Card', '2026-03-06 17:45:00'),
    (120, 'Visakhapatnam', 'Home Decor', 15.99, 'Cash', '2026-03-06 19:10:00')
]
        

    cursor.executemany('''
    INSERT OR IGNORE INTO transactions (receipt_id, store_location, item_category, price, payment_method, timestamp)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', mock_data)

    conn.commit()
    conn.close()
    print("Database 'retail_store.db' setup successfully!")

if __name__ == "__main__":
    build_database()