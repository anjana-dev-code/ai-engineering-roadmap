# Set a passing threshold
passing_grade = 50

# List of student records
students = [
    ("Alice", 85),
    ("Bob", 42),
    ("Charlie", 90),
    ("Diana", 65),
]

# count how many students passed.
passed_students = 0
for name,grade in students:
    if grade >= passing_grade:
        passed_students += 1


# top student and their score
top_student = ""
highest_grade = 0
for name, grade in students:
    if grade > highest_grade:
        highest_grade = grade
        top_student = name

print(top_student)
print(highest_grade)
    