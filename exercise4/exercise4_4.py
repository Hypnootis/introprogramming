
try:
    number1 = int(input("First number:\n"))
    number2 = int(input("Second number:\n"))
    if number2 == 0:
        print("You can't divide by zero.")
    else:
        print(number1 / number2)
except:
    print("Incorrect format.")


