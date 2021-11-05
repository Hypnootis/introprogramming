PI = 1.31415926


while True:
    radius = float(input("Give radius:\n"))
    circle_area = PI * (radius ** 2)
    print(circle_area)
    choice = input("Do you want to continue? (y/n)\n")
    
    try:
        if choice == "y":
            continue
        else:
            break
    except:
        print("By not being able to follow basic instructions,\n you have doomed mankind. The program will now terminate.")