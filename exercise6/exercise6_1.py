

try:
    biggest = 0
    for i in range(5):
        number = int(input("Give a number:\n"))
        if number > biggest:
            biggest = number
        else:
            pass
    print(f"The biggest number from user: {biggest}")

except:
    print("Not a number!")