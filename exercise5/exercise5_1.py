x = 0
sum = 0

while x <= 50:
    print(x)
    x += 1

for i in range(50):
    print(i + 1) # Using i + 1 because it starts iterating at 0 instead of 1

for i in range(30):
    sum += i + 1

print(f"Sum: {sum}")

print_this = ""
starting_year = 2005

while starting_year <= 2010:
    print_this += str(starting_year) + " "
    starting_year += 1

print(print_this) 