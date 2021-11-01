side1 = float(input("Give the first side:\n"))
side2 = float(input("Give the second side:\n"))
side3 = float(input("Give the third side:\n"))

box_volume = round(side1 * side2 * side3, 2)

print(f"Box volume: {box_volume} m3")

radius = float(input("Give the sphere radius:\n"))

sphere_volume = round((4/3) * 3.141592 * (radius ** 3), 2)

print(f"Sphere volume: {sphere_volume} m3")
