import sqlite3

# Connect to (or create) a database file
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS enrollments")
cursor.execute("DROP TABLE IF EXISTS students")

# Create the students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    major TEXT
)
""")

# Create the enrollments table
cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
)
""")

# Insert sample rows
cursor.execute("INSERT INTO students VALUES (1, 'Anjana', 'ICT')")
cursor.execute("INSERT INTO students VALUES (2, 'Raj', 'Business')")

cursor.execute("INSERT INTO enrollments VALUES (101, 1, 'Databases')")
cursor.execute("INSERT INTO enrollments VALUES (102, 1, 'Networking')")
cursor.execute("INSERT INTO enrollments VALUES (103, 2, 'Marketing')")

conn.commit()
print("Database created and populated ")

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

cursor.execute("SELECT * FROM enrollments")
print(cursor.fetchall())

cursor.execute("SELECT name FROM students")
print(cursor.fetchall())

cursor.execute("SELECT * FROM students WHERE major = 'ICT'")
print(cursor.fetchall())

cursor.execute("SELECT course FROM enrollments WHERE student_id = 1")
print(cursor.fetchall())
