import sqlite3

conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Task 1 — Subquery: employees earning above average
cursor.execute("""
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees)
""")
print(cursor.fetchall())

# Task 2 — CTE version of the same query
cursor.execute("""
WITH avg_sal AS(
    SELECT AVG(salary) AS avg_salary FROM employees
)
SELECT name, salary
FROM employees, avg_sal
WHERE salary > avg_sal.avg_salary
""")
print(cursor.fetchall())

# Task 3: Query company.db and label each employee 'High' (salary > 65000), 'Medium' (salary > 45000), or 'Low' (everything else), showing name, salary, and the label column. Use END AS salary_band to name it.
cursor.execute("""
SELECT name, salary,
   CASE
      WHEN salary > 65000 THEN 'High'
      WHEN salary > 45000 THEN 'Medium'
      ELSE 'Low'
    END AS salary_band
FROM employees
""")
print(cursor.fetchall())

# Task 4 — Window Function: rank employees by salary within each department
cursor.execute("""
SELECT name, dept_id, salary,
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS salary_rank
FROM employees
WHERE salary IS NOT NULL
""")
print(cursor.fetchall())