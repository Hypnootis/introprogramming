import math

a = float(input("Give first value:\n"))
b = float(input("Give second value:\n"))
c = float(input("Give third value:\n"))

answer1 = ((-1 * b) + math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)
answer2 = ((-1 * b) - math.sqrt((b ** 2) - 4 * a * c)) / (2 * a)

print(f"x = {answer1} and x = {answer2}")
