import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, " \
"name TEXT, " \
"category TEXT, " \
"price NUMBER, " \
"supplier_notes TEXT)")



cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_notes) " \
" VALUES (101, 'Wireless Mouse', 'Accessories', 24.99, NULL)")
cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_notes) " \
" VALUES (102, 'Mechanical Keyboard', 'Accessories', 89.00, 'Best Seller')")
cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_notes) " \
" VALUES (103, '27-inch Monitor', 'Displays', 299.99, NULL)")
cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_notes) " \
" VALUES (104, 'USB-C Hub', 'Accessories', 34.50, 'Limited Stock')")
cursor.execute("INSERT INTO products (product_id, name, category, price, supplier_notes) " \
" VALUES (105, 'Laptop Stand', 'Workspace', 39.90, NULL)")


conn.commit()
conn.close()