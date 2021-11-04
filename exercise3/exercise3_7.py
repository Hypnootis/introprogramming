# I didn't want to use a while loop for this even though I would've used it normally

item_type = str(input("Are you shipping a (P)arcel or a (L)etter:\n"))
item_weight = int(input("Give the weight of the item (in grams):\n"))

cost = 0.0

if item_type.lower() == "l":
    cost += 0.5  # Base cost for a letter
    fits = input("Does the letter fit into a mailbox? (Y/N)\n")
    if fits.lower() == "n":
        cost += 2.0  # Not fitting comes with an extra cost
    else:
        pass

elif item_type.lower() == "p":
    cost += 2.0  # Base cost for a parcel
else:
    print("Unknown type, try again")    # Doesn't really handle errors?

if 200 <= item_weight <= 500:  # Item weight between
    if item_type == "l":
        cost += ((item_weight // 100) * 0.04)
    else:
        cost += ((item_weight // 100) * 0.08)
elif item_weight > 500:
    if item_type == "l":
        cost += ((item_weight // 100) * 0.7)
    else:
        cost += ((item_weight // 100) * 0.14)

print(f"Cost of the shipment is: {cost}€")
