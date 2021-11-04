money = int(input("How many cents? (1-100)\n"))

# This next bit basically takes the floor division of the original money value
# Then substracts it as it goes on, testing to see how many coins it can fit in

fifty_cents = money // 50
money -= (fifty_cents * 50)
twenty_cents = money // 20
money -= (twenty_cents * 20)
ten_cents = money // 10
money -= (ten_cents * 10)
five_cents = money // 5
money -= (five_cents * 5)
two_cents = money // 2
money -= (two_cents * 2)

print(f"Amount of 50 cents: {fifty_cents}\n"
      f"Amount of 20 cents: {twenty_cents}\n"
      f"Amount of 10 cents: {ten_cents}\n"
      f"Amount of 5 cents: {five_cents}\n"
      f"Amount of 2 cents: {two_cents}\n"
      f"Amount of 1 cents: {money}")
