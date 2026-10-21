import sqlite3

conn = sqlite3.connect("study_tracker.db")
cur = conn.cursor()


def run(title, query):
    print(f"\n-{title}-")
    for row in cur.execute(query):
        print(row)


run("Q1: average minutes per student (top 5)", """
SELECT s.name, ROUND(AVG(ss.minutes), 1) AS avg_minutes
FROM students s
JOIN sessions ss ON ss.student_id = s.id
GROUP BY s.id
ORDER BY avg_minutes DESC
LIMIT 5;
""")

run("Q2: total minutes per subject", """
SELECT subject, SUM(minutes) AS total_minutes
FROM sessions
GROUP BY subject
ORDER BY total_minutes DESC;
""")

run("Q3: students above the overall average", """
SELECT s.name, ROUND(AVG(ss.minutes), 1) AS avg_minutes
FROM students s
JOIN sessions ss ON ss.student_id = s.id
GROUP BY s.id
HAVING AVG(ss.minutes) > (SELECT AVG(minutes) FROM sessions)
ORDER BY avg_minutes DESC;
""")

conn.close()