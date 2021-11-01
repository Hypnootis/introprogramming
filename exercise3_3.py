hours = float(input("How many workhours this week?\n"))
salary = float(input("Your hourly salary?\n"))

overtime = 0
if hours - 40 > 0:
    overtime = hours - 40

overtime_salary = overtime * (salary * 1.5)
salary = (hours - overtime) * salary
print(f"Your weekly wage: {round(overtime_salary + salary, 2)}€")
