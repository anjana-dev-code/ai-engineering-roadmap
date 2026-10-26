import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

cursor.execute("INSERT INTO employees VALUES (6, 'Noor', NULL, 1)")
conn.commit()

# Task 2 — COALESCE + flagging bad data
cursor.execute("""
SELECT name, COALESCE(salary, 0) AS salary_filled
FROM employees
""")
print(cursor.fetchall())

cursor.execute("""
SELECT name, salary,
    CASE WHEN salary IS NULL THEN 1 ELSE 0 END AS is_invalid
FROM employees
""")
print(cursor.fetchall())