import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("DROP TABLE IF EXISTS departments")

cursor.execute("""
CREATE TABLE departments(
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE employees(
   emp_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL,
   salary INTEGER,
   dept_id INTEGER,
   FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
)
""")

cursor.execute("INSERT INTO departments VALUES (1, 'Engineering')")
cursor.execute("INSERT INTO departments VALUES (2, 'Business')")
cursor.execute("INSERT INTO departments VALUES (3, 'Marketing')")

cursor.execute("INSERT INTO employees VALUES (1, 'Anna', 70000, 1)")
cursor.execute("INSERT INTO employees VALUES (2, 'Viky', 65000, 1)")
cursor.execute("INSERT INTO employees VALUES (3, 'Max', 60000, 2)")
cursor.execute("INSERT INTO employees VALUES (4, 'Lina', 50000, 3)")
cursor.execute("INSERT INTO employees VALUES (5, 'David', 40000, 2)")

conn.commit()
print("Company database created")

cursor.execute("SELECT * FROM departments")
print(cursor.fetchall())

cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

cursor.execute("INSERT INTO employees VALUES (6, 'Noor', NULL, 1)")
conn.commit()

cursor.execute("SELECT name, salary FROM employees WHERE salary IS NULL")
print(cursor.fetchall())

cursor.execute("SELECT name, salary FROM employees WHERE salary IS NOT NULL")
print(cursor.fetchall())