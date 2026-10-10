import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def run_analysis():
    # Connect to SQLite database
    conn = sqlite3.connect('retail_store.db')

   
    print("\n--- SQL: REVENUE ANALYSIS BY STORE LOCATION ---")

    query_store = """
        SELECT store_location,
               ROUND(SUM(price), 2) AS total_sales,
               COUNT(receipt_id) AS total_transactions
        FROM transactions
        GROUP BY store_location
        ORDER BY total_sales DESC;
    """

    df_store = pd.read_sql_query(query_store, conn)
    print(df_store.to_string(index=False))

    
    print("\n--- SQL: POPULAR PAYMENT METHODS ---")

    query_payment = """
        SELECT payment_method,
               COUNT(receipt_id) AS total_uses,
               ROUND(AVG(price), 2) AS average_transaction_value
        FROM transactions
        GROUP BY payment_method;
    """

    df_payment = pd.read_sql_query(query_payment, conn)
    print(df_payment.to_string(index=False))

    
    print("\n--- PANDAS: DUPLICATE DETECTION ---")

    df_all = pd.read_sql_query(
        "SELECT * FROM transactions;",
        conn
    )

    duplicate_mask = df_all.duplicated(
        subset=[
            'store_location',
            'item_category',
            'price',
            'timestamp'
        ],
        keep=False
    )

    df_duplicates = df_all[duplicate_mask]

    if not df_duplicates.empty:
        print(
            "Potential duplicate records found:",
            len(df_duplicates)
        )

        print(
            df_duplicates[
                ['receipt_id', 'store_location', 'price', 'timestamp']
            ].to_string(index=False)
        )
    else:
        print("No potential duplicate records found.")

    
    df_clean = df_all.drop_duplicates(
        subset=[
            'store_location',
            'item_category',
            'price',
            'timestamp'
        ],
        keep='first'
    ).copy()

    print("\n--- CLEANED TRANSACTION DATA ---")
    print("Original records:", len(df_all))
    print("Cleaned records:", len(df_clean))
    print("Records removed:", len(df_all) - len(df_clean))

   
    print("\n--- SALES ANALYSIS AFTER CLEANING ---")

    sales_after_cleaning = (
        df_clean.groupby('store_location')
        .agg(
            total_sales=('price', 'sum'),
            total_transactions=('receipt_id', 'count')
        )
        .reset_index()
    )

    sales_after_cleaning['total_sales'] = (
        sales_after_cleaning['total_sales'].round(2)
    )

    sales_after_cleaning = sales_after_cleaning.sort_values(
        by='total_sales',
        ascending=False
    )

    print(sales_after_cleaning.to_string(index=False))

    
    print("\n--- CREATING STORE-WISE SALES CHART ---")

    plt.figure(figsize=(8, 5))

    plt.bar(
        sales_after_cleaning['store_location'],
        sales_after_cleaning['total_sales']
    )

    plt.title('Store-wise Sales Analysis')
    plt.xlabel('Store Location')
    plt.ylabel('Total Sales')
    plt.tight_layout()

    plt.savefig('store_sales_chart.png')
    print("Chart saved as store_sales_chart.png")

    plt.show()

    
    df_clean.to_csv(
        'cleaned_transactions.csv',
        index=False
    )

    print("\nCleaned data exported successfully!")
    print("File: cleaned_transactions.csv")

    conn.close()


if __name__ == "__main__":
    run_analysis()
