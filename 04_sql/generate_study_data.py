import sqlite3
import random
from datetime import date, timedelta

random.seed (42)

conn = sqlite3.connect("study_tracker.db")
cur = conn.cursor()

cur.executescript("""
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS sessions;
CREATE TABLE students (
    id     INTEGER PRIMARY KEY,
    name   TEXT,
    course TEXT
);
CREATE TABLE sessions (
    id         INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject    TEXT,
    minutes    INTEGER,
    day        TEXT,
    FOREIGN KEY (student_id) REFERENCES students(id)
);
""")

names = ["Aisha", "Ben", "Chloe", "Dev", "Emma", "Farid", "Grace", "Hiro",
         "Ivy", "Jon", "Kira", "Leo", "Maya", "Noah", "Omar", "Priya",
         "Quinn", "Rosa", "Sam", "Tara"]
courses = ["ICT", "Business", "Cybersecurity"]
subjects = ["Python", "SQL", "Maths", "Networking", "Statistics"]

students = [(i + 1, name, random.choice(courses)) for i, name in enumerate(names)]
cur.executemany("INSERT INTO students VALUES (?, ?, ?)", students)

hard_workers = set(random.sample(range(1, 21), 5))

sessions = []
start = date(2026, 9, 1)
session_id = 1
for student_id in range(1, 21):
    n_sessions = random.randint(8, 25)
    for _ in range(n_sessions):
        base = 90 if student_id in hard_workers else 45
        minutes = max(10, int(random.gauss(base, 15)))
        day = start + timedelta(days=random.randint(0, 45))
        sessions.append((session_id, student_id, random.choice(subjects),
                         minutes, day.isoformat()))
        session_id += 1

cur.executemany("INSERT INTO sessions VALUES (?, ?, ?, ?, ?)", sessions)
conn.commit()

