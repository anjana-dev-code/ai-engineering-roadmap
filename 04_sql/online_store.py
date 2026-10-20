import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.executescript("""
CREATE TABLE customers (
    id   INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    city TEXT
);
CREATE TABLE products (
    id       INTEGER PRIMARY KEY,
    name     TEXT NOT NULL,
    category TEXT,
    price    REAL
);
CREATE TABLE orders (
    id          INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date  TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
CREATE TABLE order_items (
    order_id   INTEGER,
    product_id INTEGER,
    quantity   INTEGER,
    FOREIGN KEY (order_id)   REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
""")

customers = [
    (1, "Aisha", "Dubai"), (2, "Ben", "Perth"), (3, "Chloe", "Sydney"),
    (4, "Dev", "Dubai"), (5, "Emma", "Perth"), (6, "Farid", "Melbourne"),
    (7, "Grace", "Sydney"), (8, "Hiro", "Perth"),
]
products = [
    (1, "Laptop", "Electronics", 1200.0), (2, "Phone", "Electronics", 800.0),
    (3, "Headphones", "Electronics", 150.0), (4, "Desk", "Furniture", 300.0),
    (5, "Chair", "Furniture", 180.0), (6, "Notebook", "Stationery", 5.0),
    (7, "Pen Pack", "Stationery", 8.0), (8, "Monitor", "Electronics", 350.0),
    (9, "Lamp", "Furniture", 45.0), (10, "Backpack", "Accessories", 60.0),
]
orders = [
    (1, 1, "2026-09-01"), (2, 2, "2026-09-03"), (3, 3, "2026-09-05"),
    (4, 1, "2026-09-10"), (5, 4, "2026-09-12"), (6, 5, "2026-09-15"),
    (7, 2, "2026-09-20"), (8, 6, "2026-09-22"),
]

order_items = [
    (1, 1, 1), (1, 3, 2), (2, 2, 1), (2, 6, 10), (3, 4, 1), (3, 5, 2),
    (4, 8, 2), (4, 7, 5), (5, 10, 3), (5, 6, 4), (6, 9, 2), (6, 5, 1),
    (7, 1, 1), (7, 3, 1), (7, 8, 1), (8, 7, 6), (8, 6, 8), (8, 10, 1),
    (2, 3, 1), (5, 9, 1),
]

cur.executemany("INSERT INTO customers VALUES (?, ?, ?)", customers)
cur.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", products)
cur.executemany("INSERT INTO orders VALUES (?, ?, ?)", orders)
cur.executemany("INSERT INTO order_items VALUES (?, ?, ?)", order_items)
conn.commit()

def run(title, query):
    print(f"\n{title}")
    for row in cur.execute(query):
        print(row)

run("Revenue per product", """
SELECT p.name, SUM(oi.quantity * p.price) AS revenue
FROM order_items oi
JOIN products p ON p.id = oi.product_id
GROUP BY p.id
ORDER BY revenue DESC;
""")

run("Top 3 customers by spend", """
SELECT c.name, SUM(oi.quantity * p.price) AS total_spend
FROM customers c
JOIN orders o       ON o.customer_id = c.id
JOIN order_items oi ON oi.order_id   = o.id
JOIN products p     ON p.id          = oi.product_id
GROUP BY c.id
ORDER BY total_spend DESC
LIMIT 3;
""")

run("Customers with no orders", """
SELECT c.name
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id
WHERE o.id IS NULL;
""")

run("Categories above the overall average line value", """
SELECT p.category, AVG(oi.quantity * p.price) AS avg_line_value
FROM order_items oi
JOIN products p ON p.id = oi.product_id
GROUP BY p.category
HAVING AVG(oi.quantity * p.price) > (
    SELECT AVG(oi2.quantity * p2.price)
    FROM order_items oi2
    JOIN products p2 ON p2.id = oi2.product_id
);
""")

conn.close()