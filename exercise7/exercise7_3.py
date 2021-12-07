shopcart = [
 {"name": "Beehive - lamp", "price": 999.9},
 {"name": "Malm - bed", "price": 169.9},
 {"name": "Moomin - mug set", "price": 59.9},
 {"name": "Nemo - divan", "price": 699.9},
 {"name": "Ritz - armchair", "price": 369.9}
]

price = 0.0
print("Receipt:")
for i in shopcart:
 print("\t- " + i["name"])
 price += i["price"]

print(f"{price} €.")
print("Please come again!")
