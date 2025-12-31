import sqlite3

def filtering_null_values_with_is_null_and_is_not_null():
    # Connect to a local SQLite database (example.db)
    conn = sqlite3.connect("example.db")
    cursor = conn.cursor()

    # SQL query for Challenge #13
    query = "SELECT name, supplier_notes FROM products WHERE supplier_notes IS NULL"

    cursor.execute(query)
    rows = cursor.fetchall()

    # Print results
    for row in rows:
        print(row)

    conn.close()


if __name__ == "__main__":
    filtering_null_values_with_is_null_and_is_not_null()