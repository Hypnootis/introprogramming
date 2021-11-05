rain = []
average = 0.0

for i in range(12):
    rain_asked = float(input("Give rain amount of month:\n"))
    rain.append(rain_asked)

for i in range(len(rain)):
    average += rain[i]

average = average / len(rain)

print(f"Year average for rain = {average}")