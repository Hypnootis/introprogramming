temp = int(input("Give the temperature:\n"))

if temp < 11:
    print("COLD")
elif 10 < temp < 16:
    print("CHILLY")
elif 15 < temp < 21:
    print("QUITE WARM")
elif 20 < temp < 26:
    print("WARM")
elif 25 < temp <= 30:
    print("HOT")
