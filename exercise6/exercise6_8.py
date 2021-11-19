import random

lower_case = ["a", "b", "c", "d", "e", "f", "g",
              "h", "i", "j", "k", "l", "m", "n",
              "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z"]

upper_case = []

for i in range(len(lower_case)):
    upper_case.append(lower_case[i].upper())

numbers = ["0", "1", "2", "3", "4", "5",
           "6", "7", "8", "9"]

special_chars = ["-", "_", "~", "?", "*", "$", "#", "!", "+", "%", "@"]
all_chars = lower_case + upper_case + numbers + special_chars

while True:
    password_length = int(input("Give a password length:\n"))
    if password_length < 8:
        print("Password must be at least 8 characters long")
    else:
        password = ""
        password += random.choice(lower_case)
        password += random.choice(upper_case)
        password += random.choice(numbers)
        password += random.choice(special_chars)

        for i in range(password_length - 4):
            password += random.choice(all_chars)

        password_list = []
        for i in password:
            password_list.append(i)
        random.shuffle(password_list)
        new_password = ""

        for i in password_list:
            new_password += i

        print(new_password)
        break

