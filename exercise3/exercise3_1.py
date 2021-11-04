number1 = int(input("Give first number:\n"))
number2 = int(input("Give second number:\n"))

if number1 < number2:
    print(f"Bigger number = {number2}")
elif number2 < number1:
    print(f"Bigger number = {number1}")
else:
    print("Numbers are equal.")
