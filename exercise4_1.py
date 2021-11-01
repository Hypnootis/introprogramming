from datetime import date

today = str(date.today())
day = today[-2:]
month = today[5:7]
year = today[0:4]
name = "John Doe"
birth_year = 1984
balance = 345

new_var = f"{name} ({birth_year}), balance: {balance} €, updated on {day}.{month}.{year}."

print(new_var)
