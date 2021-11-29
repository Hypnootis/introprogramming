student_amount = int(input("How many students?\n"))
grades = []

for i in range(student_amount):
    grade = int(input("Student grade:\n"))
    grades.append(grade)

grade_average = sum(grades) / len(grades)



grade_median = 0.0

if len(grades) % 2 != 0:
    grade_median = grades[len(grades) // 2]
else:
    grade_median = (grades[(len(grades) // 2) - 1] + grades[(len(grades) // 2)]) / 2

print(f"Average grade: {grade_average}")
print(f"Median grade: {grade_median}")

if 0 <= grade_average < 1:
    print("Bad result")
elif 1 <= grade_average < 2:
    print("Weak result")
elif 2 <= grade_average < 3:
    print("Average result")
elif 3 <= grade_average < 4:
    print("Good result")
elif 4 <= grade_average <= 5:
    print("Excellent result")
