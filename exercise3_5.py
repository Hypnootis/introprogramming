points = int(input("Exam points:\n"))

grade = 0

if 0 <= points <= 50:
    grade = 0
elif 51 <= points <= 60:
    grade = 1
elif 61 <= points <= 70:
    grade = 2
elif 71 <= points <= 80:
    grade = 3
elif 81 <= points <= 90:
    grade = 4
elif 91 <= points <= 100:
    grade = 5
else:
    print("Invalid points value.")

print(f"Grade: {grade}")
