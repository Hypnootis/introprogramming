side1 = float(input("Give the first leg:\n"))
side2 = float(input("Give the second leg:\n"))

hypotenuse = (side1 ** 2) + (side2 ** 2)
hypotenuse = round(hypotenuse ** 0.5, 2)

print(f"Hypotenuse: {hypotenuse} m")
