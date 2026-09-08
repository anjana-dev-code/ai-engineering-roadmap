import numpy as np 

grades = np.array([[85, 90, 78],
                    [92, 88, 95],
                    [70, 75, 80],
                    [88, 92, 85]])

print("Grades matrix:\n", grades)
print("Shape:", grades.shape) 

student_avg = grades.mean(axis=1)
print("Student averages:", student_avg)

subject_avg = grades.mean(axis=0)
print("Subject averages:", subject_avg)

print("Transposed:\n", grades.T)