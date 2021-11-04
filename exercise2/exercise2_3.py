salary = float(input("Your monthly salary:\n"))
tax_prc = float(input("Your tax percentage:\n"))

tax = salary * (tax_prc * 0.01)
earnings = salary - tax

print(f"Earnings: {earnings} €\nTaxes: {tax} €")
