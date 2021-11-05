cities = ["Rome", "Athens", "Stockholm", "London", "Dublin", "Paris"]
cities = sorted(cities)

for i in range(len(cities)):
    print(f"{i + 1}. {cities[i]}")   # i+1 for the list index, then cities[i] to access the city name
