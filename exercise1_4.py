minutes = int(input("Give minutes:\n"))

hours = minutes // 60
minutes = minutes % 60

print(f"{hours}h {minutes}min")