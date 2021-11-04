driven_non_urban = float(input("Kilometers outside urban area:\n"))
driven_urban = float(input("Kilometers within urban area:\n"))

# 5.1l outside urban area, 7.5l inside urban area (per 100km)

consumption = (driven_non_urban / 100) * 5.1 + ((driven_urban / 100) * 7.5)

print(f"Consumption: {consumption} l")
