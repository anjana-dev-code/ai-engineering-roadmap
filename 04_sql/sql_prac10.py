import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS enrollments")
cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("DROP TABLE IF EXISTS courses")

cursor.execute("""
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    major TEXT
)
""")

cursor.execute("""
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    credits INTEGER
)
""")

cursor.execute("""
CREATE TABLE enrollments (
    enrollment_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
    )
""")

# Students
cursor.execute("INSERT INTO students VALUES (1, 'Anjana', 'ICT')")
cursor.execute("INSERT INTO students VALUES (2, 'Raj', 'Business')")
cursor.execute("INSERT INTO students VALUES (3, 'Jack', 'ICT')")

# Courses
cursor.execute("INSERT INTO courses VALUES (101, 'Databases', 3 )")
cursor.execute("INSERT INTO courses VALUES (102, 'Networking', 4 )")
cursor.execute("INSERT INTO courses VALUES (103, 'Marketing', 3 )")

# Enrollments
cursor.execute("INSERT INTO enrollments VALUES (1, 1, 101)")
cursor.execute("INSERT INTO enrollments VALUES (2, 1, 102)")
cursor.execute("INSERT INTO enrollments VALUES (3, 2, 103)")

conn.commit()
print("Joins practice data ready")

cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

cursor.execute("SELECT * FROM courses")
print(cursor.fetchall())

cursor.execute("SELECT * FROM enrollments")
print(cursor.fetchall())

#LEFT JOIN: see Jack actually appear with a NULL
cursor.execute("""
SELECT s.name, c.course_name
FROM students s
LEFT JOIN enrollments e ON s.student_id = e.student_id
LEFT JOIN courses c ON e.course_id = c.course_id
""")
print(cursor.fetchall())