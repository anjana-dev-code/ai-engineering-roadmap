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
cursor.execute("INSERT INTO employees VALUES (7, 'Sam', 55000, 3)")
cursor.execute("INSERT INTO employees VALUES (8, 'Priya', 80000, 1)")
cursor.execute("INSERT INTO employees VALUES (9, 'Ali', 45000, 3)")

conn.commit()
print("Company database created")

cursor.execute("SELECT * FROM departments")
print(cursor.fetchall())

cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

# Problem 1:Get the names of all employees earning more than 55000, sorted from highest to lowest salary.
cursor.execute("""
SELECT name 
FROM employees
WHERE salary > 55000           
ORDER BY salary DESC; 
""")
print(cursor.fetchall())

# Problem 2:Find all employees whose name starts with the letter 'A' or 'S'.
cursor.execute("""
SELECT name FROM employees
WHERE name LIKE 'A%' OR name LIKE 'S%'
ORDER BY name;
""")
print(cursor.fetchall())

# Problem 3:For each department, show the department ID and how many employees are in it — but only show departments with more than 2 employees.
cursor.execute("""
SELECT dept_id, COUNT(*)
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 2
ORDER BY dept_id;
""")
print(cursor.fetchall())

# Problem 4: Get the department with the single highest total salary bill — just the dept_id and the total (hint: you'll need ORDER BY + LIMIT 1 alongside GROUP BY).
cursor.execute("""
SELECT dept_id, AVG(salary) AS avg_salary
FROM employees 
WHERE salary > 45000
GROUP BY dept_id
HAVING avg_salary > 55000
ORDER BY avg_salary DESC
LIMIT 1;
""")
print(cursor.fetchall())