money = int(input("Give money:\n"))
cost = int(input("Purchase cost:\n"))

if cost - money > 0:
    money = money + int(input("Not enough money, give more:\n"))
if cost - money > 0:
    print("You don't have enough money.")

if cost - money <= 0:
    print(f"Thank you. Here's the change: {money - cost}€")
