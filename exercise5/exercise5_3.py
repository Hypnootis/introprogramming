from math import pi

while True:
    try:
        radius = int(input("Give radius:\n"))
        circle_area = pi * (radius ** 2)
        circle_area = round(circle_area, 2)
        print(circle_area)

        choice = input("Do you want to continue? (y/n)\n")
        if choice == "n":
            break
        else:
            pass

    except:
        pass
