from math import pi

running = True
while running:
    try:
        radius = float(input("Give radius:\n"))
        circle_area = pi * (radius ** 2)
        circle_area = round(circle_area, 2)
        print(circle_area)

        awaiting_input = True

        while awaiting_input:
            choice = input("Do you want to continue? (y/n)\n")
            if choice == "y":
                break
            elif choice == "n":
                running = False
                break
            else:
                pass

    except:
        pass

