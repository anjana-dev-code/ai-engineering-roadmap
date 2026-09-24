import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Task 1 — Find duplicates + standardize text

# Task 1a: find duplicate names (exact match)
cursor.execute("""
SELECT name, COUNT(*) AS cnt
FROM employees
GROUP BY name
HAVING COUNT(*) > 1
""")
print(cursor.fetchall())

# Task 1b: standardize the messy names
cursor.execute("""
SELECT DISTINCT TRIM(LOWER(name)) AS clean_name
FROM employees
""")
print(cursor.fetchall())

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

#Task 3 — Index + EXPLAIN
cursor.execute("CREATE INDEX IF NOT EXISTS idx_dept_id ON employees(dept_id)")
conn.commit()

cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM employees WHERE dept_id = 1")
print(cursor.fetchall())