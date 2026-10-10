
import sqlite3
import pandas as pd

conn = sqlite3.connect("retail_store.db")

with open("analysis_queries.sql", "r", encoding="utf-8") as file:
    sql_content = file.read()

queries = [
    query.strip()
    for query in sql_content.split(";")
    if query.strip()
]

for number, query in enumerate(queries, start=1):
    print(f"\n{'=' * 50}")
    print(f"QUERY {number} RESULTS")
    print("=" * 50)

    try:
        result = pd.read_sql_query(query, conn)
        print(result.to_string(index=False))
    except Exception as error:
        print(f"Error: {error}")

conn.close()
