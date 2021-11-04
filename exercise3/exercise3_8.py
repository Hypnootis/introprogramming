cost = float(input("Give the cost of the order:\n"))
total_cost = 0
is_student = False
is_vip = False
vip_points = 0
shipping = 0
if cost <= 99:
    shipping = 7.95
sales_code = input("Input a possible sales code\n").lower()

if input("Are you a student? (Y/N)\n").lower() == "y":
    is_student = True
else:
    is_student = False

if input("Are you a VIP customer? (Y/N)\n").lower() == "y":
    is_vip = True
    vip_points = int(input("How many VIP points do you have?\n"))
else:
    is_vip = False

if sales_code == "fall21":
    total_cost = (cost * 0.9)
elif sales_code == "bk2school" and is_student:
    total_cost = (cost * 0.8)

if is_vip:
    if vip_points > 0:
        use_points = input(f"Would you like to use your VIP points on this order? (Y/N)\n").lower()
        if use_points == "y":
            total_cost -= ((vip_points // 1000) * 5)

if is_vip:
    vip_points += ((total_cost // 10) * 100)

total_cost += shipping

print(f"Total cost of your purchase is {total_cost}€, including shipping")
