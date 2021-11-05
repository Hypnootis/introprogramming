months = ("January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December")

try:
    choice = int(input("Give the number of month:\n"))
    print(months[choice - 1])

except:
    pass
